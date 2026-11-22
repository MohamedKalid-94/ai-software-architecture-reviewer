from datetime import datetime
from pydantic import BaseModel


class ReviewSchema(BaseModel):

    id: str

    project_id: str

    document_id: str

    status: str = "CREATED"

    reviewer: str | None = None

    started_at: datetime | None = None

    completed_at: datetime | None = None