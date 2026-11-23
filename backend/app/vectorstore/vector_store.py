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