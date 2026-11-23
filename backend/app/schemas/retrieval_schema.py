from pydantic import BaseModel


class RetrievalRequest(BaseModel):

    query: str

    top_k: int = 5



class RetrievalResponse(BaseModel):

    chunk_id: str

    document_id: str

    content: str

    score: float