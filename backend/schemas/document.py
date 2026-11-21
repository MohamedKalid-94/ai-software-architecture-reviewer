from datetime import datetime

from pydantic import BaseModel


class DocumentMetadata(BaseModel):

    document_id: str
    filename: str
    file_path: str
    file_size: int
    file_type: str
    uploaded_at: datetime