from fastapi import APIRouter, File, UploadFile

from backend.schemas.upload import UploadResponse
from backend.services.upload_service import UploadService
from backend.services.metadata_service import MetadataService


router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


upload_service = UploadService()

metadata_service = MetadataService()


@router.post(
    "",
    response_model=UploadResponse,
)
async def upload_document(
    file: UploadFile = File(...),
):

    saved_file = upload_service.save_file(file)

    metadata = metadata_service.generate(
        saved_file
    )


    return UploadResponse(

        message="File uploaded successfully",

        document=metadata,
    )