from fastapi import APIRouter, UploadFile, File


from backend.app.services.document_service import (
    DocumentService
)



router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


service = DocumentService()



@router.post("/upload")
async def upload_document(
    project_id: str,
    file: UploadFile = File(...)
):


    result = service.upload_document(
        file,
        project_id
    )


    return {

        "message": "Document uploaded successfully",

        "document": result

    }