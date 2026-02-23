import spacy
from spacy.matcher import Matcher

from app.entity_extractor import extract_date_range, extract_date_entities, detect_query_type
from app.intent_registry import INTENT_REGISTRY
from app.models import IntentResult
from app.remove_aux_tokens import remove_aux
from app.scorer import calculate_confidence

nlp = spacy.load("en_core_web_sm")


class IntentEngine:

    def __init__(self):
        self.matcher = Matcher(nlp.vocab)
        self._register_patterns()

    def _register_patterns(self):
        for intent_id, config in INTENT_REGISTRY.items():
            for pattern in config["patterns"]:
                self.matcher.add(intent_id, [pattern])

    def detect_intent(self, text: str) -> IntentResult:
        text = remove_aux(text)
        doc = nlp(text)
        matches = self.matcher(doc)

        if not matches:
            return IntentResult(
                intent_id="unknown",
                entities={},
                query_type="unknown",
                confidence=0.0
            )

        # Choose highest priority intent
        scored = []

        for match_id, start, end in matches:
            intent_id = nlp.vocab.strings[match_id]
            priority = INTENT_REGISTRY[intent_id]["priority"]
            scored.append((intent_id, priority))

        scored.sort(key=lambda x: x[1], reverse=True)
        best_intent = scored[0][0]
        priority = scored[0][1]

        date_range = extract_date_entities(doc)

        confidence = calculate_confidence(len(matches), priority)

        return IntentResult(
            intent_id=best_intent,
            entities={"date_range": date_range} if date_range else {},
            query_type= detect_query_type(doc),
            confidence=confidence
        )
