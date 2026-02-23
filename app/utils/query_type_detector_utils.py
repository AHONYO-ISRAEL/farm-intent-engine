import spacy

nlp = spacy.load("en_core_web_sm")


def is_ranking(doc):
    return any(token.tag_ == "JJS" for token in doc)


def is_comparison(doc):
    comparative = any(token.tag_ == "JJR" for token in doc)
    has_than = any(token.lower_ == "than" for token in doc)
    compare_words = {"compare", "versus", "vs", "between"}
    has_compare_word = any(token.lemma_ in compare_words for token in doc)
    return comparative or has_than or has_compare_word


def is_trend(doc):
    trend_verbs = {"increase", "decrease", "grow", "decline", "rise", "fall", "change"}
    return any(token.lemma_ in trend_verbs for token in doc)


def is_average(doc):
    average_words = {"average", "mean"}
    return any(token.lemma_ in average_words for token in doc)


def is_yes_no(doc):
    return doc[0].pos_ == "AUX"


def is_absolute(doc):
    for i in range(len(doc) - 1):
        if doc[i].lower_ == "how" and doc[i + 1].lower_ == "many":
            return True
    return False


QUERY_TYPE_RULES = {
    "ranking": is_ranking,
    "comparison": is_comparison,
    "trend": is_trend,
    "average": is_average,
    "yes_no": is_yes_no,
    "aggregate_absolute": is_absolute,
}
