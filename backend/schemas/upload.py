from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    file_size: int
    message: str