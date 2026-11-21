from pydantic import BaseModel


class DocumentChunk(BaseModel):

    chunk_id: str

    content: str

    chunk_size: int

    chunk_index: int