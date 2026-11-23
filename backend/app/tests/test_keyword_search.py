from backend.app.services.keyword_search_service import (
    KeywordSearchService
)



service = KeywordSearchService()



chunks = [

    {
        "chunk_id":"CH001",
        "document_id":"DOC001",
        "content":
        "Database replication improves scalability"
    },


    {
        "chunk_id":"CH002",
        "document_id":"DOC001",
        "content":
        "Frontend application uses React framework"
    },


    {
        "chunk_id":"CH003",
        "document_id":"DOC001",
        "content":
        "Kubernetes manages container deployment"
    }

]


service.build_index(
    chunks
)


results = service.search(
    "database scalability"
)


assert len(results) > 0


assert results[0]["chunk_id"] == "CH001"


print(
    "Keyword search validation passed ✅"
)