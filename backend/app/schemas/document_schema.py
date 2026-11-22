from datetime import datetime
from pydantic import BaseModel

class DocumentUploadSchema(BaseModel):
    project_id: str
    filename: str
    document_type: str

class DocumentResponseSchema(BaseModel):
    id: str
    project_id: str
    filename: str
    document_type: str
    storage_path: str
    status: str
    uploaded_at: datetime