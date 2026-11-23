from fastapi import APIRouter


from backend.app.services.chunk_service import (
    ChunkService
)


router = APIRouter(
    prefix="/chunks",
    tags=["Chunking"]
)


service = ChunkService()



@router.post("/create")
async def create_chunks(
    document_id: str,
    text: str
):

    return service.create_document_chunks(

        document_id,

        text

    )