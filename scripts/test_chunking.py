from backend.services.chunking_service import ChunkingService



def main():

    service = ChunkingService()


    text = """

    System Architecture Overview

    The application contains frontend,
    backend and AI processing components.

    Backend uses FastAPI.

    AI workflow uses LangGraph.

    """


    chunks = service.create_chunks(

        text=text,

        document_id="doc-001",

        filename="architecture.pdf",

        page_number=3,

        heading="System Architecture"

    )


    print("\nGenerated Chunks\n")


    for chunk in chunks:

        print("--------------------")

        print("Chunk ID:")
        print(chunk.chunk_id)

        print("\nContent:")
        print(chunk.content)

        print("\nMetadata:")
        print(chunk.metadata)



if __name__ == "__main__":

    main()