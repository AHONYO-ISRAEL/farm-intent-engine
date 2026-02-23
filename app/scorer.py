def calculate_confidence(match_count, priority):
    base = match_count * 10
    score = base + priority
    return min(score / 100, 1.0)