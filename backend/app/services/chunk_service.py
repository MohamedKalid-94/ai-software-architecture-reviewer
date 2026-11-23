import uuid


from backend.app.processors.text_chunk_processor import (
    TextChunkProcessor
)


from backend.app.services.text_processing_service import (
    TextProcessingService
)



class ChunkService:


    def __init__(self):

        self.processor = TextChunkProcessor()

        self.text_service = TextProcessingService()



    def create_document_chunks(
        self,
        document_id,
        text
    ):


        normalized_text = (
            self.text_service.normalize_text(
                text
            )
        )


        chunks = (
            self.processor.create_chunks(
                normalized_text
            )
        )


        results = []


        for chunk in chunks:

            results.append(

                {
                    "chunk_id": str(uuid.uuid4()),

                    "document_id": document_id,

                    "content": chunk,

                    "token_count": len(
                        chunk.split()
                    )

                }

            )


        return results