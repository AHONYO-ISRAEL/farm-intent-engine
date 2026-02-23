INTENT_REGISTRY = {
    "track_egg_production": {
        "patterns": [
            [{"LEMMA": "egg"}, {"LEMMA": {"IN": ["collect", "produce", "lay"]}}]
        ],
        "query_type": "absolute",
        "priority": 5
    },
    "track_eggs_sold": {
        "patterns": [
            [{"LEMMA": "sell"}, {"OP": "*"}, {"LEMMA": "egg"}],
            [{"LEMMA": "egg"}, {"OP": "*"}, {"LEMMA": "sell"}],
            [{"LEMMA": "egg"}, {"OP": "*"}, {"LEMMA": "sale"}],
        ],
        "query_type": "absolute",
        "priority": 7
    },
    "monitor_mortality": {
        "patterns": [
            [{"LEMMA": {"IN": ["mortality", "death", "die"]}}]
        ],
        "query_type": "rate",
        "priority": 6
    }
}
