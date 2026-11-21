from pydantic import BaseModel
from backend.schemas.heading import DocumentHeading


class StructuredDocument(BaseModel):

    filename: str

    total_pages: int

    headings: list[DocumentHeading]

    extracted_text: str

class ParsedDocument(BaseModel):

    filename: str

    total_pages: int

    extracted_text: str