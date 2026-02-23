from rich import print
from app.intent_egine import IntentEngine

engine = IntentEngine()

while True:
    query = input("\nAsk something: ")
    result = engine.detect_intent(query)
    print(result.model_dump_json(indent=2))