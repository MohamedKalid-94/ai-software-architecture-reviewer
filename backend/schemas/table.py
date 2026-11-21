from pydantic import BaseModel


class ExtractedTable(BaseModel):

    page_number: int

    rows: list[list[str | None]]