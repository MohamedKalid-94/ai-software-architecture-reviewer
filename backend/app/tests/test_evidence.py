from backend.app.schemas.evidence_schema import EvidenceCreateSchema
from backend.app.services.evidence_service import EvidenceService

def test_evidence_creation():

    service = EvidenceService()

    evidence = EvidenceCreateSchema(
        document_id="DOC001",
        page="12",
        section="Database",
        content="No database replication configured"
    )

    result = service.create_evidence(evidence)

    assert result.document_id == "DOC001"

    print("Evidence validation passed ✅")

if __name__ == "__main__":
    test_evidence_creation()