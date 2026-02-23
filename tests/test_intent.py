import pytest
import spacy
from spacy.matcher import Matcher

from app.intent_registry import INTENT_REGISTRY


@pytest.fixture(scope="module")
def nlp():
    return spacy.load("en_core_web_sm")


@pytest.fixture(scope="module")
def matcher(nlp):
    matcher = Matcher(nlp.vocab)

    for intent_name, config in INTENT_REGISTRY.items():
        matcher.add(intent_name, config["patterns"])

    return matcher


def detect_intent(doc, matcher):
    matches = matcher(doc)

    if not matches:
        return None

    # choose highest priority intent
    scored = []
    for match_id, start, end in matches:
        intent_name = doc.vocab.strings[match_id]
        priority = INTENT_REGISTRY[intent_name]["priority"]
        scored.append((priority, intent_name))

    scored.sort(reverse=True)
    return scored[0][1]


# ==========================================================
# 1️⃣ FLOCK INTENTS
# ==========================================================

@pytest.mark.parametrize("text", [
    "How many birds do we have?",
    "What is the current bird count?",
    "Show me the number of birds."
])
def test_track_bird_count(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_bird_count"


@pytest.mark.parametrize("text", [
    "How many birds died this week?",
    "Show mortality rate.",
    "Bird deaths yesterday."
])
def test_monitor_mortality(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "monitor_mortality"


@pytest.mark.parametrize("text", [
    "How many birds were culled?",
    "Culling rate for this batch.",
    "Remove birds from flock."
])
def test_monitor_culling(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "monitor_culling"


@pytest.mark.parametrize("text", [
    "What is the survival rate?",
    "How many survived?",
    "Bird survival statistics."
])
def test_evaluate_survival_rate(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "evaluate_survival_rate"


# ==========================================================
# 2️⃣ EGG INTENTS
# ==========================================================

@pytest.mark.parametrize("text", [
    "How many eggs were produced today?",
    "Egg production this week.",
    "How many eggs did we collect?"
])
def test_track_egg_production(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_egg_production"


@pytest.mark.parametrize("text", [
    "Which flock produced the most eggs?",
    "Egg output per cage.",
    "Eggs per batch."
])
def test_track_egg_production_per_flock(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_egg_production_per_flock"


@pytest.mark.parametrize("text", [
    "Egg quality report.",
    "How many broken eggs?",
    "Cracked eggs today."
])
def test_monitor_egg_quality(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "monitor_egg_quality"


@pytest.mark.parametrize("text", [
    "Hatch success rate?",
    "How many chicks hatched?",
    "Hatch rate this month."
])
def test_track_hatch_success(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_hatch_success"


# ==========================================================
# 3️⃣ CHICK INTENTS
# ==========================================================

@pytest.mark.parametrize("text", [
    "How many chicks are available?",
    "Available chick pool.",
    "Number of chicks ready."
])
def test_check_available_chicks(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "check_available_chicks"


@pytest.mark.parametrize("text", [
    "Assign chicks to flock 3.",
    "Chick transfer report.",
    "Move chicks to another cage."
])
def test_track_assigned_chicks(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_assigned_chicks"


# ==========================================================
# 4️⃣ FEED INTENTS
# ==========================================================

@pytest.mark.parametrize("text", [
    "Feed stock status.",
    "How much feed is left?",
    "Current feed inventory."
])
def test_monitor_feed_stock(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "monitor_feed_stock"


@pytest.mark.parametrize("text", [
    "Feed efficiency report.",
    "What is the FCR?",
    "Feed conversion ratio?"
])
def test_evaluate_feed_efficiency(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "evaluate_feed_efficiency"


@pytest.mark.parametrize("text", [
    "When will feed run out?",
    "Do we need more feed?",
    "Order feed for next week."
])
def test_forecast_feed_need(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "forecast_feed_need"


# ==========================================================
# 5️⃣ SALES INTENTS
# ==========================================================

@pytest.mark.parametrize("text", [
    "How many eggs were sold today?",
    "Egg sales this week.",
    "Did we sell eggs yesterday?"
])
def test_track_eggs_sold(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_eggs_sold"


@pytest.mark.parametrize("text", [
    "What is total revenue?",
    "How much money did we make?",
    "Sales revenue this month."
])
def test_track_revenue(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_revenue"


# ==========================================================
# 6️⃣ HEALTH INTENTS
# ==========================================================

@pytest.mark.parametrize("text", [
    "Vaccination schedule?",
    "Medication given to flock?",
    "Treat birds with antibiotics."
])
def test_track_vaccines_meds(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "track_vaccines_meds"


@pytest.mark.parametrize("text", [
    "Why did birds die?",
    "Cause of death?",
    "Reason for mortality?"
])
def test_diagnose_mortality_causes(nlp, matcher, text):
    doc = nlp(text)
    assert detect_intent(doc, matcher) == "diagnose_mortality_causes"