from backend.app.schemas import (
    ProjectCreateSchema,
    DocumentUploadSchema,
    ReviewCreateSchema
)



def test_project_schema():

    project = ProjectCreateSchema(
        name="Architecture Review",
        description="AI architecture analysis"
    )


    assert project.name == "Architecture Review"



def test_document_schema():

    document = DocumentUploadSchema(
        project_id="P001",
        filename="architecture.pdf",
        document_type="pdf"
    )


    assert document.filename == "architecture.pdf"



def test_review_schema():

    review = ReviewCreateSchema(
        project_id="P001",
        document_id="DOC001"
    )


    assert review.project_id == "P001"


if __name__ == "__main__":

    test_project_schema()

    test_document_schema()

    test_review_schema()

    print(
        "All schema validations passed ✅"
    )