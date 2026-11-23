from fastapi import APIRouter

from backend.app.schemas.retrieval_schema import (
    RetrievalRequest
)

from backend.app.services.hybrid_retrieval_service import (
    HybridRetrievalService
)



router = APIRouter(

    prefix="/retrieval",

    tags=["Retrieval"]

)



service = HybridRetrievalService()



@router.post("/search")
async def search(
    request: RetrievalRequest
):

    return service.search(

        request.query,

        request.top_k

    )