from pathlib import Path
import shutil
import uuid

from fastapi import HTTPException, UploadFile, status

from backend.core.logging import logger
from backend.core.settings import settings
from backend.services.validation_service import ValidationService


class UploadService:

    def __init__(self):

        self.upload_dir = Path(settings.UPLOAD_DIR)
        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.validation_service = ValidationService()

    def validate_file(
        self,
        file: UploadFile,
    ):

        extension = Path(file.filename).suffix.lower()

        allowed_extensions = [
            f".{ext.strip().lower()}"
            for ext in settings.ALLOWED_EXTENSIONS.split(",")
        ]

        if extension not in allowed_extensions:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF files are allowed.",
            )

    def validate_size(
        self,
        file: UploadFile,
    ):

        file.file.seek(0, 2)
        size = file.file.tell()
        file.file.seek(0)

        max_size = (
            settings.MAX_UPLOAD_SIZE_MB
            * 1024
            * 1024
        )

        if size > max_size:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Maximum file size is {settings.MAX_UPLOAD_SIZE_MB} MB.",
            )

    def save_file(
        self,
        file: UploadFile,
    ) -> Path:

        # Extension validation
        self.validate_file(file)

        # Size validation
        self.validate_size(file)

        # Generate unique filename
        unique_name = (
            f"{uuid.uuid4()}_{file.filename}"
        )

        destination = (
            self.upload_dir / unique_name
        )

        # Save file
        with destination.open("wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        # Validate PDF
        validation = (
            self.validation_service.validate_pdf(
                destination
            )
        )

        if not validation["valid"]:

            destination.unlink(
                missing_ok=True
            )

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=validation["reason"],
            )

        # Generate SHA256 hash
        file_hash = (
            self.validation_service.generate_file_hash(
                destination
            )
        )

        # Duplicate detection
        if self.validation_service.check_duplicate(
            file_hash
        ):

            destination.unlink(
                missing_ok=True
            )

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Duplicate document detected.",
            )

        # Register document
        self.validation_service.register_document(
            document_id=str(uuid.uuid4()),
            filename=destination.name,
            file_hash=file_hash,
        )

        logger.info(
            f"Uploaded: {destination.name}"
        )

        return destination