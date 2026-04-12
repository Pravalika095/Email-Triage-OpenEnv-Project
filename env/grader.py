def grade(prediction, expected):
    score = 0
    total = len(expected)

    for key in expected:
        if key in prediction and prediction[key] == expected[key]:
            score += 1

    if total == 0:
        return 0.5

    base_score = score / total

    final_score = 0.3 + (base_score * 0.4)

    # ensure strictly inside (0,1)
    if final_score >= 1.0:
        final_score = 0.99
    if final_score <= 0.0:
        final_score = 0.01

    return final_score