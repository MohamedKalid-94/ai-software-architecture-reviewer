from datetime import datetime
from pydantic import BaseModel


class EvaluationSchema(BaseModel):

    id: str

    review_id: str

    metric_name: str

    metric_score: float

    evaluator_type: str

    details: str | None = None

    created_at: datetime