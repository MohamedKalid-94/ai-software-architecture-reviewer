from datetime import datetime

from pydantic import BaseModel


class DocumentMetadata(BaseModel):

    filename: str

    file_type: str

    file_size: int

    storage_path: str

    uploaded_at: datetime

    status: str