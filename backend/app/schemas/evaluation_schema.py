from pydantic import BaseModel



class EvaluationResponseSchema(BaseModel):

    id: str

    metric_name: str

    metric_score: float

    evaluator_type: str