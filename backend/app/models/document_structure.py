from pydantic import BaseModel


class PageMetadata(BaseModel):
    page_number: int
    character_count: int
    word_count: int


class Heading(BaseModel):
    page_number: int
    text: str
    level: int


class Section(BaseModel):
    title: str
    start_page: int
    end_page: int