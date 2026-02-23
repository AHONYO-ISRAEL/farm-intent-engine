def remove_aux(text: str) -> str:
    """
    Remove common English auxiliary verbs from a text string.

    Args:
        text (str): Input text.

    Returns:
        str: Text with auxiliary verbs removed.
    """
    # Common auxiliary verbs
    aux_verbs = {
        "am", "is", "are", "was", "were",
        "be", "been", "being",
        "do", "does", "did",
        "have", "has", "had",
        "will", "would", "shall", "should",
        "can", "could", "may", "might", "must"
    }

    # Tokenize by whitespace
    tokens = text.split()

    # Filter out auxiliaries (case-insensitive)
    filtered_tokens = [t for t in tokens if t.lower() not in aux_verbs]

    # Rejoin into a string
    return " ".join(filtered_tokens)

