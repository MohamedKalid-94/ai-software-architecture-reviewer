class ResultFusionService:


    def fuse(
        self,
        vector_results,
        keyword_results
    ):

        combined = {}


        # Add vector results

        for result in vector_results:

            chunk_id = result["chunk_id"]

            combined[chunk_id] = {

                **result,

                "vector_score":
                result.get(
                    "score",
                    0
                ),

                "keyword_score": 0

            }



        # Add keyword results

        for result in keyword_results:

            chunk_id = result["chunk_id"]


            if chunk_id in combined:

                combined[chunk_id][
                    "keyword_score"
                ] = result.get(
                    "keyword_score",
                    0
                )


            else:

                combined[chunk_id] = {

                    **result,

                    "vector_score":0,

                    "keyword_score":
                    result.get(
                        "keyword_score",
                        0
                    )

                }



        results = []


        for item in combined.values():

            item["fusion_score"] = (

                item["vector_score"] * 0.5

                +

                item["keyword_score"] * 0.5

            )

            results.append(item)

        results.sort(

            key=lambda x:
            x["fusion_score"],

            reverse=True

        )
        return results