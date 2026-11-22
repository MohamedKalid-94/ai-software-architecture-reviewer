from datetime import datetime
from pydantic import BaseModel, Field


class ProjectSchema(BaseModel):

    id: str = Field(
        description="Unique project identifier"
    )

    name: str = Field(
        description="Project name"
    )

    description: str | None = None

    owner_id: str

    created_at: datetime

    updated_at: datetime