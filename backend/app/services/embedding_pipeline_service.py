from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.vector_index_service import VectorIndexService


class EmbeddingPipelineService:


    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.index_service = VectorIndexService()


    def embed_chunks(
        self,
        chunks
    ):

        texts = []


        for chunk in chunks:

            if "content" not in chunk:

                raise ValueError(
                    "Chunk content field is required"
                )

            texts.append(
                chunk["content"]
            )


        embeddings = self.embedding_service.generate_embeddings(
            texts
        )


        results = []


        for chunk, vector in zip(
            chunks,
            embeddings
        ):

            embedded_chunk = {

                **chunk,

                "embedding": vector

            }


            # Store vector in index
            self.index_service.index_embedding(
                embedded_chunk
            )


            results.append(
                embedded_chunk
            )


        return results