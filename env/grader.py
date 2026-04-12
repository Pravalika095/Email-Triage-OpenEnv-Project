def grade(prediction, expected):
    score = 0
    total = len(expected)

    for key in expected:
        if key in prediction and prediction[key] == expected[key]:
            score += 1

    if total == 0:
        return 0.5  # safe fallback

    raw_score = score / total

    # ✅ FIX: keep score strictly between (0,1)
    if raw_score == 1.0:
        return 0.9
    elif raw_score == 0.0:
        return 0.1
    else:
        return raw_score