from backend.app.services.chunk_service import (
    ChunkService
)



def test_chunk_creation():

    service = ChunkService()


    chunks = service.create_document_chunks(

        "DOC-001",

        "This is a sample architecture document."

    )


    assert len(chunks) > 0

    assert chunks[0]["document_id"] == "DOC-001"


    print(
        "Chunk creation validation passed ✅"
    )



if __name__ == "__main__":

    test_chunk_creation()