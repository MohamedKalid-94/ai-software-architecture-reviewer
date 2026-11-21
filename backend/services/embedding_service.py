from backend.embeddings.ollama_embedding import (
    OllamaEmbeddingProvider
)


class EmbeddingService:


    def __init__(self):

        self.provider = (
            OllamaEmbeddingProvider()
        )


    def create_embedding(
        self,
        text: str
    ):

        return self.provider.generate(
            text
        )