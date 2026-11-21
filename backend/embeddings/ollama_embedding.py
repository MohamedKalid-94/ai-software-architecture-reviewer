from langchain_ollama import OllamaEmbeddings

from backend.core.settings import settings


class OllamaEmbeddingProvider:


    def __init__(self):

        self.embedding = OllamaEmbeddings(

            model=settings.EMBEDDING_MODEL,

            base_url=settings.OLLAMA_BASE_URL

        )


    def generate(self, text: str):

        return self.embedding.embed_query(
            text
        )


    def generate_documents(
        self,
        texts: list[str]
    ):

        return self.embedding.embed_documents(
            texts
        )