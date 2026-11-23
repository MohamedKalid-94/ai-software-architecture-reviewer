from fastapi import APIRouter

from backend.app.schemas.embedding_schema import (
    ChunkEmbeddingRequest
)

from backend.app.services.embedding_pipeline_service import (
    EmbeddingPipelineService
)


router = APIRouter(
    prefix="/embeddings",
    tags=["Embeddings"]
)


service = EmbeddingPipelineService()


@router.post("/generate")
async def generate_embeddings(
    chunks: list[ChunkEmbeddingRequest]
):

    return service.embed_chunks(
        [
            chunk.model_dump()
            for chunk in chunks
        ]
    )