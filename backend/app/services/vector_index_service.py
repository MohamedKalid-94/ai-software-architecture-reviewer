from backend.app.vectorstore.vector_store import VectorStore


class VectorIndexService:


    def __init__(self):

        self.vector_store = VectorStore()



    def index_embedding(
        self,
        embedded_chunk
    ):


        return self.vector_store.add_vector(

            chunk_id=embedded_chunk["chunk_id"],

            document_id=embedded_chunk["document_id"],

            embedding=embedded_chunk["embedding"],

            metadata={
                "token_count":
                embedded_chunk.get(
                    "token_count"
                )
            }

        )


    def get_index():

        return self.vector_store.get_vectors()