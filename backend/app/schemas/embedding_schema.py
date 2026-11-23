from pydantic import BaseModel


class ChunkEmbeddingRequest(BaseModel):

    chunk_id: str

    document_id: str

    content: str

    token_count: int