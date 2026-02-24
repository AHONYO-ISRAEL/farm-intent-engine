from pydantic import BaseModel
from typing import Optional, Dict

class DateRange(BaseModel):
    start: str
    end : str

class IntentResult(BaseModel):
    intent_id: str
    entities: Dict
    query_type: str
    confidence: float

class Query(BaseModel):
    text: str