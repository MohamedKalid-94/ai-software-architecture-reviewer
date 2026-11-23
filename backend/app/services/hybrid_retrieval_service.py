from backend.app.services.vector_search_service import (
    VectorSearchService
)

from backend.app.services.keyword_search_service import (
    KeywordSearchService
)

from backend.app.services.result_fusion_service import (
    ResultFusionService
)

from backend.app.services.ranking_service import (
    RankingService
)



class HybridRetrievalService:


    def __init__(self):

        self.vector_service = VectorSearchService()

        self.keyword_service = KeywordSearchService()

        self.fusion_service = ResultFusionService()

        self.ranking_service = RankingService()



    def search(
        self,
        query,
        top_k=5
    ):


        vector_results = (
            self.vector_service.search(
                query,
                top_k
            )
        )


        keyword_results = (
            self.keyword_service.search(
                query,
                top_k
            )
        )


        fused_results = (
            self.fusion_service.fuse(
                vector_results,
                keyword_results
            )
        )


        ranked_results = (
            self.ranking_service.rank(
                fused_results
            )
        )


        return ranked_results[:top_k]