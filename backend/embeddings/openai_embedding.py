from langchain_openai import OpenAIEmbeddings

from backend.core.settings import settings



class OpenAIEmbeddingProvider:


    def __init__(self):

        self.embedding = OpenAIEmbeddings(

            model=settings.EMBEDDING_MODEL,

            api_key=settings.OPENAI_API_KEY,

        )


    def generate(
        self,
        text: str
    ):

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