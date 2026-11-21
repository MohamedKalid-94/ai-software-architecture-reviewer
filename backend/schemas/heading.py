from pydantic import BaseModel


class DocumentHeading(BaseModel):

    title: str

    level: int

    page_number: int