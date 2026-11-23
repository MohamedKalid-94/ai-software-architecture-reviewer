from backend.app.services.vector_search_service import (
    VectorSearchService
)


service = VectorSearchService()


chunks = [

    {
        "chunk_id":"CH001",
        "document_id":"DOC001",
        "content":
        "Database uses replication for scalability",
        "embedding":[0.1,0.2,0.3]
    },

    {
        "chunk_id":"CH002",
        "document_id":"DOC001",
        "content":
        "Frontend uses React framework",
        "embedding":[0.8,0.7,0.6]
    }

]


for chunk in chunks:

    service.index_service.index_embedding(
        chunk
    )


result = service.search(
    "database scalability"
)


assert len(result) > 0


print(
    "Vector search validation passed ✅"
)