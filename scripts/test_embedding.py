from backend.services.embedding_service import (
    EmbeddingService
)



def main():


    service = EmbeddingService()


    text = """
    FastAPI provides backend API services
    for the AI Software Architecture Reviewer.
    """


    vector = service.create_embedding(
        text
    )


    print(
        "Vector dimension:",
        len(vector)
    )


    print(
        "First 10 values:"
    )


    print(
        vector[:10]
    )



if __name__ == "__main__":

    main()