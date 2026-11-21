from fastapi import APIRouter, File, UploadFile

from backend.schemas.upload import UploadResponse
from backend.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

upload_service = UploadService()


@router.post(
    "",
    response_model=UploadResponse,
)
async def upload_document(
    file: UploadFile = File(...),
):

    saved_file = upload_service.save_file(file)

    return UploadResponse(
        filename=saved_file.name,
        file_size=saved_file.stat().st_size,
        message="File uploaded successfully",
    )