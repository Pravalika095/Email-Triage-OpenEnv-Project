def grade(pred, expected):
    score = 0.0

    if pred.get("category") == expected.get("category"):
        score += 0.4

    if pred.get("priority") == expected.get("priority"):
        score += 0.3

    if pred.get("department") == expected.get("department"):
        score += 0.3

    return score