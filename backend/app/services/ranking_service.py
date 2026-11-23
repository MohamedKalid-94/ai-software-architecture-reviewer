class RankingService:


    def rank(
        self,
        results
    ):


        ranked_results = []


        for item in results:


            vector_score = item.get(
                "vector_score",
                0
            )


            keyword_score = item.get(
                "keyword_score",
                0
            )


            metadata_score = self.metadata_score(
                item
            )


            final_score = (

                vector_score * 0.5

                +

                keyword_score * 0.3

                +

                metadata_score * 0.2

            )


            item["final_score"] = final_score


            ranked_results.append(
                item
            )



        ranked_results.sort(

            key=lambda x:
            x["final_score"],

            reverse=True

        )


        return ranked_results



    def metadata_score(
        self,
        item
    ):

        metadata = item.get(
            "metadata",
            {}
        )


        if metadata:

            return 1


        return 0