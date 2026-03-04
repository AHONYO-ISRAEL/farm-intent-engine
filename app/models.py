from typing import Dict

from pydantic import BaseModel


class DateRange(BaseModel):
    start: str
    end: str


class IntentResult(BaseModel):
    intent_id: str
    query_type: str
    meta: Dict
    filters: Dict


class Query(BaseModel):
    text: str
