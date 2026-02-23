import spacy
from spacy import displacy
from spacy.matcher import Matcher


# -----------------------------
# Function Definitions
# -----------------------------

def load_nlp_model(model_name='en_core_web_sm'):
    """Load the spaCy NLP pipeline."""
    return spacy.load(model_name)


def process_text(nlp, text):
    """Process the text with the NLP pipeline and return a doc object."""
    return nlp(text)


def tokenize(doc):
    """Print the part-of-speech tag for each token."""
    print("TOKENS & POS TAGS:")
    for token in doc:
        print(token.pos_)
    print("-" * 40)


def named_entity_recognition(doc):
    """Print entities with their label and character positions."""
    print("NAMED ENTITIES:")
    for ent in doc.ents:
        print(ent.text, ent.label_, ent.start_char, ent.end_char)
    print("-" * 40)


def get_date_name_entities(doc):
    date_entities = [
        ent.text
        for ent in doc.ents
        if ent.label_ == "DATE"
    ]
    print("DATE ENTITIES ", date_entities)
    return date_entities



def sentence_segmentation(doc):
    """Print each sentence in the doc."""
    print("SENTENCES:")
    for sent in doc.sents:
        print(sent.text)
    print("-" * 40)


def display_with_displacy(doc, style='dep'):
    """Serve visualizations using displacy."""
    # style='dep' for dependency, 'ent' for entities
    displacy.serve(doc, style=style)


def similarity_check(doc1, doc2):
    """Print similarity between two docs."""
    print(f"Similarity between '{doc1.text}' and '{doc2.text}': {doc2.similarity(doc1):.2f}")
    print("-" * 40)


def matcher_example(nlp, doc):
    """Run a matcher example for 'Israel love' pattern."""
    print("MATCHING:")
    matcher = Matcher(nlp.vocab)
    pattern = [{"LOWER": "israel"}, {"LEMMA": "love"}]
    matcher.add("APPLE_BUY", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        print(doc[start:end])
    print("-" * 40)


def print_lemmas(doc):
    """Print lemmas of non-stopword tokens."""
    print("LEMMA OF NON-STOPWORDS:")
    for token in doc:
        if not token.is_stop:
            print(token.text, "->", token.lemma_)
    print("-" * 40)


def remove_aux_tokens(doc):
    """
    Return text from doc with all AUX (auxiliary verbs) removed.
    """
    filtered_tokens = [token.text for token in doc if token.pos_ != "AUX"]
    return " ".join(filtered_tokens)


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == '__main__':
    # Load NLP model
    nlp = load_nlp_model()

    # Example text
    text = 'Apple were looking at buying startup in San Francisco today and three weeks ago '
    doc = process_text(nlp, text)

    # Run functions
    tokenize(doc)
    named_entity_recognition(doc)
    get_date_name_entities(doc)
    sentence_segmentation(doc)
    # display_with_displacy(doc, style='dep')  # Uncomment to visualize dependency
    # display_with_displacy(doc, style='ent')  # Uncomment to visualize entities
    print_lemmas(doc)

    # Another docs for matcher and similarity
    doc1 = process_text(nlp, "Israel loving oranges and loves Macarena")
    doc2 = process_text(nlp, "I enjoy apples")

    # similarity_check(doc1, doc2)  # Uncomment to check similarity

    matcher_example(nlp, doc1)

    print("Original Text:")
    print(doc.text)

    cleaned_text = remove_aux_tokens(doc)
    print("\nText without AUX tokens:")
    print(cleaned_text)
