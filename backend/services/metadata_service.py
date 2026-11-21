from datetime import datetime
from pathlib import Path
import uuid

from backend.schemas.document import DocumentMetadata


class MetadataService:


    def generate(
        self,
        file_path: Path,
    ) -> DocumentMetadata:

        return DocumentMetadata(

            document_id=str(uuid.uuid4()),

            filename=file_path.name,

            file_path=str(file_path),

            file_size=file_path.stat().st_size,

            file_type=file_path.suffix.replace(".", ""),

            uploaded_at=datetime.utcnow(),
        )