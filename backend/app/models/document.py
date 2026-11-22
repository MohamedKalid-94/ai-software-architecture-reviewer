from datetime import datetime
from pydantic import BaseModel, Field


class DocumentSchema(BaseModel):

    id: str

    project_id: str

    filename: str

    document_type: str

    storage_path: str

    uploaded_by: str

    uploaded_at: datetime

    processed: bool = False