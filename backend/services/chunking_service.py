from backend.chunking.recursive_splitter import RecursiveSplitter



class ChunkingService:


    def __init__(self):

        self.splitter = RecursiveSplitter()



    def create_chunks(
        self,
        text: str,
        document_id: str,
        filename: str,
        page_number=None,
        heading=None,
    ):


        return self.splitter.split(

            text=text,

            document_id=document_id,

            filename=filename,

            page_number=page_number,

            heading=heading,

        )