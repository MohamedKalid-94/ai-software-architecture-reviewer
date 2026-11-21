from pydantic import BaseModel


class ChunkMetadata(BaseModel):

    document_id: str

    filename: str

    page_number: int | None = None

    heading: str | None = None



class DocumentChunk(BaseModel):

    chunk_id: str

    parent_id: str

    content: str

    chunk_size: int

    chunk_index: int

    metadata: ChunkMetadata