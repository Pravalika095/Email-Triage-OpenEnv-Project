def grade(prediction, expected):
    score = 0
    total = len(expected)

    for key in expected:
        if key in prediction and prediction[key] == expected[key]:
            score += 1

    return score / total if total > 0 else 0.0