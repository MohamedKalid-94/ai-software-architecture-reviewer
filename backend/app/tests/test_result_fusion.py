from backend.app.services.result_fusion_service import (
    ResultFusionService
)



service = ResultFusionService()



vector_results = [

    {
        "chunk_id":"CH001",
        "document_id":"DOC001",
        "content":
        "Database replication",
        "score":0.9
    }

]


keyword_results = [

    {
        "chunk_id":"CH001",
        "document_id":"DOC001",
        "content":
        "Database replication",
        "keyword_score":0.8
    },


    {
        "chunk_id":"CH002",
        "document_id":"DOC001",
        "content":
        "Database indexing",
        "keyword_score":0.6
    }

]


results = service.fuse(

    vector_results,

    keyword_results

)


assert len(results) == 2


assert results[0]["chunk_id"] == "CH001"


print(
    "Result fusion validation passed ✅"
)