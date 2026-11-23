from backend.app.services.embedding_service import (
    EmbeddingService
)

from backend.app.services.vector_index_service import (
    VectorIndexService
)


class VectorSearchService:


    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.index_service = VectorIndexService()



    def search(
        self,
        query,
        top_k=5
    ):

        query_embedding = (
            self.embedding_service
            .generate_embeddings(
                [query]
            )[0]
        )


        results = (
            self.index_service
            .search(
                query_embedding,
                top_k
            )
        )


        return results