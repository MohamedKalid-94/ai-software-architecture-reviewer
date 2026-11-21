from sentence_transformers import SentenceTransformer


class LocalEmbeddingProvider:


    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def generate(self, text):

        return self.model.encode(
            text
        ).tolist()


    def generate_documents(self, texts):

        return self.model.encode(
            texts
        ).tolist()