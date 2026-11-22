from datetime import datetime
from pydantic import BaseModel


class FindingSchema(BaseModel):

    id: str

    review_id: str

    category: str

    title: str

    description: str

    severity: str

    confidence_score: float

    recommendation: str

    evidence_reference: str

    created_at: datetime