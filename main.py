from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.intent_egine import IntentEngine
from app.models import Query
from fastapi.middleware.cors import CORSMiddleware

from middleware.auth import verify_api_key

origins = [
    "https://your-frontend.com",
    "http://localhost:3000"
]




app = FastAPI()
engine = IntentEngine()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Intent engine running", "status": "ok"}


@app.post("/predict")
def predict(query: Query, token_data=Depends(verify_api_key)):
    return engine.detect_intent(query.text)
