from backend.chunking.parent_child_splitter import ParentChildSplitter



class ParentChildService:


    def __init__(self):

        self.splitter = ParentChildSplitter()



    def create_hierarchy(

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