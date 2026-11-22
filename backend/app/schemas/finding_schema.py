from pydantic import BaseModel



class FindingResponseSchema(BaseModel):

    id: str

    category: str

    title: str

    severity: str

    confidence_score: float

    recommendation: str

    evidence_reference: str