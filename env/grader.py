def grade(prediction, expected):
    score = 0
    total = len(expected)

    for key in expected:
        if key in prediction:
            if prediction[key] == expected[key]:
                score += 1
            else:
                score += 0.0  # ❗ no partial credit

    if total == 0:
        return 0.5

    final_score = score / total

    # ✅ clamp strictly inside (0,1)
    if final_score >= 1.0:
        final_score = 0.85
    elif final_score <= 0.0:
        final_score = 0.15

    return final_score