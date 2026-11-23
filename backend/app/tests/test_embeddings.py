from backend.app.services.embedding_service import (
    EmbeddingService
)



def test_embedding_generation():

    service = EmbeddingService()


    vector = service.generate_embedding(
        "Architecture review platform"
    )


    assert len(vector) > 0


    print(
        "Embedding generation validation passed ✅"
    )



if __name__ == "__main__":

    test_embedding_generation()