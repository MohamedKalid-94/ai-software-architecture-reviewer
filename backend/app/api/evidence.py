from fastapi import APIRouter

from backend.app.schemas.evidence_schema import (
    EvidenceCreateSchema
)

from backend.app.services.evidence_service import (
    EvidenceService
)


router = APIRouter(
    prefix="/evidence",
    tags=["Evidence"]
)


service = EvidenceService()



@router.post("/create")
async def create_evidence(
    evidence: EvidenceCreateSchema
):

    return service.create_evidence(
        evidence
    )



@router.get("/{document_id}")
async def get_evidence(
    document_id: str
):

    return service.retrieve_evidence(
        document_id
    )