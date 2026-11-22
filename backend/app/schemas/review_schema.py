from pydantic import BaseModel



class ReviewCreateSchema(BaseModel):

    project_id: str

    document_id: str



class ReviewResponseSchema(BaseModel):

    id: str

    project_id: str

    document_id: str

    status: str