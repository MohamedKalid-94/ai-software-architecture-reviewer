from langchain_ollama import OllamaEmbeddings

from backend.app.config.settings import settings



class EmbeddingService:


    def __init__(self):

        self.embeddings = OllamaEmbeddings(

            model=settings.EMBEDDING_MODEL,

            base_url=settings.OLLAMA_BASE_URL

        )


    def generate_embedding(
        self,
        text: str
    ):

        return self.embeddings.embed_query(
            text
        )


    def generate_embeddings(
        self,
        texts: list[str]
    ):

        return self.embeddings.embed_documents(
            texts
        )
        