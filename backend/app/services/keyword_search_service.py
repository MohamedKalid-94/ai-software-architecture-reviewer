from rank_bm25 import BM25Okapi


class KeywordSearchService:


    def __init__(self):

        self.documents = []

        self.bm25 = None



    def build_index(
        self,
        chunks
    ):

        self.documents = chunks


        tokenized_documents = [

            chunk["content"]
            .lower()
            .split()

            for chunk in chunks

        ]


        self.bm25 = BM25Okapi(
            tokenized_documents
        )



    def search(
        self,
        query,
        top_k=5
    ):

        if not self.bm25:

            return []


        query_tokens = (
            query
            .lower()
            .split()
        )


        scores = self.bm25.get_scores(
            query_tokens
        )


        results = []


        for index, score in enumerate(scores):

            results.append(

                {
                    **self.documents[index],
                    "keyword_score": float(score)
                }

            )


        results.sort(

            key=lambda x:
            x["keyword_score"],

            reverse=True

        )


        return results[:top_k]