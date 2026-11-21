from pydantic import BaseModel


class ParentChunk(BaseModel):

    parent_id: str

    content: str

    document_id: str

    metadata: dict