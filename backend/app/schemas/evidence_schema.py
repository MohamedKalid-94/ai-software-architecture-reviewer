from pydantic import BaseModel


class EvidenceCreateSchema(BaseModel):

    document_id: str

    page: str

    section: str

    content: str



class EvidenceResponseSchema(BaseModel):

    id: str

    document_id: str

    page: str

    section: str

    content: str