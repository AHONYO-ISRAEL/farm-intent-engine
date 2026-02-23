from app.utils.date_extractor_utils import extract_date_range
from app.utils.query_type_detector_utils import QUERY_TYPE_RULES


def extract_date_entities(doc):
    """
    Extract exactly one DATE entity and return its range.
    """
    date_entities = [
        ent.text.strip()
        for ent in doc.ents
        if ent.label_ == "DATE"
    ]
    if len(date_entities) != 1:
        return None

    return extract_date_range(date_entities[0])


def detect_query_type(doc) -> str:
    for query_type, rule_function in QUERY_TYPE_RULES.items():
        if rule_function(doc):
            return query_type

    return "aggregate_absolute"
