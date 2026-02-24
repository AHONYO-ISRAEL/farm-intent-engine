from fastapi import FastAPI
from pydantic import BaseModel

from app.intent_egine import IntentEngine
from app.models import Query

app = FastAPI()
engine = IntentEngine()


@app.get("/")
def root():
    return {"message": "Intent engine running", "status": "ok"}


@app.post("/predict")
def predict(query: Query):
    return engine.detect_intent(query.text)
