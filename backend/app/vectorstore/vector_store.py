import math


class VectorStore:

    def __init__(self):

        self.vectors = []


    def add_vector(
        self,
        chunk_id,
        document_id,
        embedding,
        metadata
    ):

        vector_record = {

            "chunk_id": chunk_id,

            "document_id": document_id,

            "embedding": embedding,

            "metadata": metadata

        }

        self.vectors.append(
            vector_record
        )


        return vector_record


    def get_vectors(self):

        return self.vectors


    def count(self):

        return len(self.vectors)



    def search(
        self,
        query_embedding,
        top_k=5
    ):

        results = []


        for vector in self.vectors:

            score = self.cosine_similarity(
                query_embedding,
                vector["embedding"]
            )


            results.append(

                {
                    **vector,
                    "score": score
                }

            )


        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return results[:top_k]



    def cosine_similarity(
        self,
        vector_a,
        vector_b
    ):

        dot_product = sum(
            a * b
            for a, b in zip(
                vector_a,
                vector_b
            )
        )


        magnitude_a = math.sqrt(
            sum(
                a * a
                for a in vector_a
            )
        )


        magnitude_b = math.sqrt(
            sum(
                b * b
                for b in vector_b
            )
        )


        if magnitude_a == 0 or magnitude_b == 0:

            return 0


        return (
            dot_product /
            (magnitude_a * magnitude_b)
        )