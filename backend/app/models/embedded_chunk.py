from pydantic import BaseModel



class EmbeddedChunk(BaseModel):

    chunk_id: str

    document_id: str

    content: str

    embedding: list[float]

    token_count: int