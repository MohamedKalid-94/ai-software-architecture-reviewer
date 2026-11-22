from pydantic import BaseModel


class DocumentTable(BaseModel):

    page_number: int

    rows: list[list[str]]