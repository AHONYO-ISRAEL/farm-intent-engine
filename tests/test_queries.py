from app.intent_egine import IntentEngine

engine = IntentEngine()

def test_egg_production():
    result = engine.detect_intent("How many eggs were collected today?")
    assert result.intent_id == "track_egg_production"

def test_eggs_sold():
    result = engine.detect_intent("How many eggs were sold yesterday?")
    assert result.intent_id == "track_eggs_sold"

def test_mortality():
    result = engine.detect_intent("What is the mortality rate?")
    assert result.intent_id == "monitor_mortality"