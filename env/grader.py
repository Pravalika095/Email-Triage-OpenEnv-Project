def grade(prediction, expected):
    score = 0.0

    if prediction.get("category") == expected.get("category"):
        score += 0.5

    if prediction.get("priority") == expected.get("priority"):
        score += 0.25

    if prediction.get("department") == expected.get("department"):
        score += 0.25

    return score