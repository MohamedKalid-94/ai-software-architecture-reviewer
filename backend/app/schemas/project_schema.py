from datetime import datetime

from pydantic import BaseModel, Field



class ProjectCreateSchema(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100
    )

    description: str | None = None



class ProjectResponseSchema(BaseModel):

    id: str

    name: str

    description: str | None = None

    owner_id: str

    created_at: datetime

    updated_at: datetime