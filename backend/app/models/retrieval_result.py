class RetrievalResult:

    def __init__(
        self,
        chunk_id,
        document_id,
        content,
        score
    ):

        self.chunk_id = chunk_id
        self.document_id = document_id
        self.content = content
        self.score = score