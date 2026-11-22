from backend.app.repositories.document_repository import (
    DocumentRepository
)



def test_document_repository():

    repository = DocumentRepository()


    document = repository.create(
        {
            "filename": "architecture.pdf",
            "project_id": "ARCH-001",
            "status": "COMPLETED"
        }
    )


    assert document["project_id"] == "ARCH-001"

    assert document["status"] == "COMPLETED"



if __name__ == "__main__":

    test_document_repository()

    print(
        "Document upload flow validation passed ✅"
    )