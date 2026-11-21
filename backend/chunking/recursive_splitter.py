import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.core.settings import settings
from backend.schemas.chunk import (
    DocumentChunk,
    ChunkMetadata,
)



class RecursiveSplitter:


    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=settings.CHUNK_SIZE,

            chunk_overlap=settings.CHUNK_OVERLAP,

            separators=[
                "\n\n",
                "\n",
                ".",
                " ",
                ""
            ]
        )



    def split(
        self,
        text: str,
        document_id: str,
        filename: str,
        page_number: int | None = None,
        heading: str | None = None,
        parent_id: str | None = None,
    ) -> list[DocumentChunk]:


        chunks = self.splitter.split_text(text)


        result = []


        for index, chunk in enumerate(chunks):

            result.append(

                DocumentChunk(

                    chunk_id=str(
                        uuid.uuid4()
                    ),

                    parent_id=parent_id,
                    content=chunk,
                    chunk_size=len(chunk),
                    chunk_index=index,
                    metadata=ChunkMetadata(
                        document_id=document_id,
                        filename=filename,
                        page_number=page_number,
                        heading=heading,

                    )

                )
            )


        return result