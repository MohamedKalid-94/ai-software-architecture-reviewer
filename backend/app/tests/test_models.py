from datetime import datetime

from backend.app.models import (
    ProjectSchema,
    DocumentSchema,
    ReviewSchema,
    FindingSchema,
    EvaluationSchema
)



def test_project_model():

    project = ProjectSchema(
        id="P001",
        name="ArchAI Reviewer",
        description="AI Architecture Review Platform",
        owner_id="USER001",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    assert project.name == "ArchAI Reviewer"



def test_document_model():

    document = DocumentSchema(
        id="DOC001",
        project_id="P001",
        filename="architecture.pdf",
        document_type="PDF",
        storage_path="/documents/architecture.pdf",
        uploaded_by="USER001",
        uploaded_at=datetime.now()
    )

    assert document.filename == "architecture.pdf"



def test_review_model():

    review = ReviewSchema(
        id="REV001",
        project_id="P001",
        document_id="DOC001"
    )

    assert review.status == "CREATED"



def test_finding_model():

    finding = FindingSchema(
        id="F001",
        review_id="REV001",
        category="Security",
        title="Missing RBAC",
        description="Authorization controls missing",
        severity="HIGH",
        confidence_score=0.92,
        recommendation="Implement RBAC",
        evidence_reference="Security Design Page 12",
        created_at=datetime.now()
    )

    assert finding.confidence_score == 0.92



def test_evaluation_model():

    evaluation = EvaluationSchema(
        id="E001",
        review_id="REV001",
        metric_name="Faithfulness",
        metric_score=0.95,
        evaluator_type="LangSmith",
        created_at=datetime.now()
    )

    assert evaluation.metric_score == 0.95



if __name__ == "__main__":

    test_project_model()
    test_document_model()
    test_review_model()
    test_finding_model()
    test_evaluation_model()

    print("All domain model validations passed ✅")