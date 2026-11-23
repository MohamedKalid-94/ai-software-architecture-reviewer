from backend.app.vectorstore.vector_store import (
    VectorStore
)


def test_vector_storage():

    store = VectorStore()


    result = store.add_vector(

        chunk_id="CH001",

        document_id="DOC001",

        embedding=[
            0.1,
            0.2,
            0.3
        ],

        metadata={
            "page":1
        }

    )


    assert result["chunk_id"] == "CH001"

    assert store.count() == 1


    print(
        "Vector storage validation passed ✅"
    )


if __name__ == "__main__":

    test_vector_storage()