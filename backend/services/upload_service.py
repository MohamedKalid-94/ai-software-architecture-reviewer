from pathlib import Path
import shutil

from fastapi import UploadFile

from backend.core.settings import settings


class UploadService:

    def __init__(self):
        self.upload_dir = Path(settings.UPLOAD_DIR)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def save_file(self, file: UploadFile) -> Path:
        """
        Save uploaded file to disk.
        """

        destination = self.upload_dir / file.filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return destination