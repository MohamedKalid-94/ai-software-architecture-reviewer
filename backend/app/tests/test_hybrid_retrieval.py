from backend.app.services.hybrid_retrieval_service import (
    HybridRetrievalService
)


service = HybridRetrievalService()



results = service.search(

    "database scalability",

    3

)



assert results is not None


print(
    "Hybrid retrieval validation passed ✅"
)