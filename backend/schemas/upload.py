from pydantic import BaseModel
from backend.schemas.document import DocumentMetadata


class UploadResponse(BaseModel):

    message: str
    document: DocumentMetadata