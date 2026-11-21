import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.schemas.chunk import DocumentChunk
from backend.schemas.parent_chunk import ParentChunk
from backend.schemas.chunk import ChunkMetadata



class ParentChildSplitter:


    def __init__(self):

        self.parent_splitter = RecursiveCharacterTextSplitter(

            chunk_size=2000,

            chunk_overlap=200,

        )


        self.child_splitter = RecursiveCharacterTextSplitter(

            chunk_size=500,

            chunk_overlap=100,

        )



    def split(

        self,

        text: str,

        document_id: str,

        filename: str,

        page_number=None,

        heading=None,

    ):


        parents = []


        children = []


        parent_chunks = self.parent_splitter.split_text(
            text
        )


        for parent_text in parent_chunks:


            parent_id = str(
                uuid.uuid4()
            )


            parent = ParentChunk(

                parent_id=parent_id,

                content=parent_text,

                document_id=document_id,

                metadata={

                    "filename": filename,

                    "page_number": page_number,

                    "heading": heading,

                }

            )


            parents.append(parent)



            child_chunks = self.child_splitter.split_text(
                parent_text
            )


            for index, child_text in enumerate(child_chunks):


                children.append(

                    DocumentChunk(

                        chunk_id=str(
                            uuid.uuid4()
                        ),

                        parent_id=parent_id,

                        content=child_text,

                        chunk_size=len(child_text),

                        chunk_index=index,

                        metadata=ChunkMetadata(

                            document_id=document_id,

                            filename=filename,

                            page_number=page_number,

                            heading=heading,

                        )

                    )

                )


        return {

            "parents": parents,

            "children": children,

        }