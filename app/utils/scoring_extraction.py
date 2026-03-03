comparative = lambda doc: any(token.tag_ == "JJR" for token in doc)

has_than = lambda doc: any(token.lower_ == "than" for token in doc)

compare_words =  {"compare", "versus", "vs", "between"}
has_compare_word =lambda doc: any(token.lemma_ in compare_words for token in doc)