from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunkProcessor:


    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200

        )


    def create_chunks(
        self,
        text
    ):

        chunks = self.splitter.split_text(
            text
        )

        return chunks