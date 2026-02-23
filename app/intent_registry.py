INTENT_REGISTRY = {

    # ===============================
    # 1️⃣ FLOCK INTENTS
    # ===============================

    "track_bird_count": {
        "patterns": [
            # how many birds
            [{"LOWER": "how"}, {"LOWER": "many"}, {"LEMMA": "bird"}],

            # current bird count / bird count
            [{"LEMMA": "bird"}, {"LEMMA": "count"}],

            # active flock
            [{"LOWER": "active"}, {"LEMMA": "flock"}],

            # number of birds
            [{"LEMMA": "number"}, {"LOWER": "of"}, {"LEMMA": "bird"}],
        ],
        "priority": 5
    },

    "monitor_mortality": {
        "patterns": [
            [{"LEMMA": "mortality"}],

            # birds died / bird die
            [{"LEMMA": "bird"}, {"LEMMA": "die", "POS": "VERB"}],

            # death rate
            [{"LEMMA": "death"}, {"LEMMA": "rate"}],

            # how many birds died
            [{"LOWER": "how"}, {"LOWER": "many"}, {"LEMMA": "bird"}, {"OP": "*"}, {"LEMMA": "die"}],
        ],
        "priority": 8
    },

    "monitor_culling": {
        "patterns": [
            [{"LEMMA": "cull"}],
            [{"LEMMA": "culling"}, {"LEMMA": "rate"}],

            # remove birds
            [{"LEMMA": "remove"}, {"OP": "*"}, {"LEMMA": "bird"}],
        ],
        "priority": 6
    },

    "evaluate_survival_rate": {
        "patterns": [
            [{"LEMMA": "survival"}, {"LEMMA": "rate"}],
            [{"LEMMA": "survive", "POS": "VERB"}],
            [{"LOWER": "how"}, {"LOWER": "many"}, {"LEMMA": "survive"}],
        ],
        "priority": 5
    },

    # ===============================
    # 2️⃣ EGG INTENTS
    # ===============================

    "track_egg_production": {
        "patterns": [
            # how many eggs produced
            [{"LOWER": "how"}, {"LOWER": "many"}, {"LEMMA": "egg"}],

            # produce eggs
            [{"LEMMA": "produce", "POS": "VERB"}, {"OP": "*"}, {"LEMMA": "egg"}],

            # eggs produced (passive)
            [{"LEMMA": "egg"}, {"OP": "*"}, {"LEMMA": "produce"}],

            # egg collection
            [{"LEMMA": "egg"}, {"LEMMA": "collection"}],
        ],
        "priority": 7
    },

    "track_egg_production_per_flock": {
        "patterns": [
            # eggs per cage/batch/flock
            [{"LEMMA": "egg"}, {"OP": "*"}, {"LEMMA": {"IN": ["cage", "batch", "flock"]}}],

            # which flock produced most eggs
            [
                {"LOWER": "which"},
                {"LEMMA": "flock"},
                {"OP": "*"},
                {"LOWER": {"IN": ["most", "more", "highest"]}},
                {"OP": "*"},
                {"LEMMA": "egg"}
            ],
        ],
        "priority": 9
    },

    "monitor_egg_quality": {
        "patterns": [
            [{"LEMMA": "egg"}, {"LEMMA": "quality"}],

            [{"LEMMA": {"IN": ["broken", "crack", "cracked", "damage"]}}, {"LEMMA": "egg"}],

            # defective eggs
            [{"LEMMA": {"IN": ["defective", "spoiled"]}}, {"LEMMA": "egg"}],
        ],
        "priority": 6
    },

    "track_hatch_success": {
        "patterns": [
            [{"LEMMA": "hatch"}, {"OP": "*"}, {"LEMMA": "success"}],

            [{"LOWER": "how"}, {"LOWER": "many"}, {"LEMMA": "chick"}, {"OP": "*"}, {"LEMMA": "hatch"}],

            # hatch rate
            [{"LEMMA": "hatch"}, {"LEMMA": "rate"}],
        ],
        "priority": 7
    },

    # ===============================
    # 3️⃣ CHICK INTENTS
    # ===============================

    "check_available_chicks": {
        "patterns": [
            [{"LEMMA": "available"}, {"LEMMA": "chick"}],

            [{"LEMMA": "chick"}, {"LEMMA": "pool"}],

            [{"LOWER": "how"}, {"LOWER": "many"}, {"LEMMA": "chick"}],
        ],
        "priority": 6
    },

    "track_assigned_chicks": {
        "patterns": [
            [{"LEMMA": "assign"}, {"OP": "*"}, {"LEMMA": "chick"}],
            [{"LEMMA": "chick"}, {"OP": "*"}, {"LEMMA": "move"}],
            [{"LEMMA": "transfer"}, {"OP": "*"}, {"LEMMA": "chick"}],
        ],
        "priority": 6
    },

    # ===============================
    # 4️⃣ FEED INTENTS
    # ===============================

    "monitor_feed_stock": {
        "patterns": [
            [{"LEMMA": "feed"}, {"LEMMA": "stock"}],

            [{"LOWER": "how"}, {"LOWER": "much"}, {"LEMMA": "feed"}],

            # feed left
            [{"LEMMA": "feed"}, {"OP": "*"}, {"LEMMA": "leave"}],
        ],
        "priority": 7
    },

    "evaluate_feed_efficiency": {
        "patterns": [
            [{"LEMMA": "feed"}, {"LEMMA": "efficiency"}],
            [{"LOWER": "fcr"}],
            [{"LEMMA": "feed"}, {"OP": "*"}, {"LEMMA": "conversion"}],
        ],
        "priority": 8
    },

    "forecast_feed_need": {
        "patterns": [
            [{"LEMMA": "order"}, {"OP": "*"}, {"LEMMA": "feed"}],

            [{"LEMMA": "need"}, {"OP": "*"}, {"LEMMA": "feed"}],

            # when will feed run out
            [{"LOWER": "when"}, {"OP": "*"}, {"LEMMA": "feed"}, {"OP": "*"}, {"LEMMA": "run"}, {"LOWER": "out"}],
        ],
        "priority": 8
    },

    # ===============================
    # 5️⃣ SALES INTENTS
    # ===============================

    "track_eggs_sold": {
        "patterns": [
            # sell eggs
            [{"LEMMA": "sell", "POS": "VERB"}, {"OP": "*"}, {"LEMMA": "egg"}],

            # eggs sold (passive)
            [{"LEMMA": "egg"}, {"OP": "*"}, {"LEMMA": "sell"}],

            # egg sales
            [{"LEMMA": "egg"}, {"LEMMA": "sale"}],
        ],
        "priority": 7
    },

    "track_revenue": {
        "patterns": [
            [{"LEMMA": "revenue"}],

            [{"LEMMA": "total"}, {"LEMMA": "sale"}],

            [{"LOWER": "how"}, {"LOWER": "much"}, {"LEMMA": {"IN": ["money", "revenue"]}}],
        ],
        "priority": 7
    },

    # ===============================
    # 6️⃣ HEALTH INTENTS
    # ===============================

    "track_vaccines_meds": {
        "patterns": [
            [{"LEMMA": "vaccine"}],
            [{"LEMMA": "medication"}],
            [{"LEMMA": "treat"}, {"OP": "*"}, {"LEMMA": {"IN": ["flock", "bird"]}}],
        ],
        "priority": 8
    },

    "diagnose_mortality_causes": {
        "patterns": [
            [{"LOWER": "why"}, {"OP": "*"}, {"LEMMA": "die"}],

            [{"LEMMA": "cause"}, {"OP": "*"}, {"LEMMA": "death"}],

            [{"LEMMA": "reason"}, {"OP": "*"}, {"LEMMA": "mortality"}],
        ],
        "priority": 9
    }
}