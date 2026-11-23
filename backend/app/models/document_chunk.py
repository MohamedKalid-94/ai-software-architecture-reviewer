from pydantic import BaseModel


class DocumentChunk(BaseModel):

    chunk_id: str

    document_id: str

    content: str

    page_number: int | None = None

    section: str | None = None

    token_count: int