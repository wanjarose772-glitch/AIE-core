def wallet_rating(score):

    if score >= 90:
        return "ELITE"

    if score >= 75:
        return "STRONG"

    if score >= 60:
        return "GOOD"

    if score >= 40:
        return "AVERAGE"

    return "POOR"