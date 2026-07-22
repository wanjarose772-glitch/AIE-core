def calculate_confidence(token):

    confidence = (
        token["alpha_score"] * 0.35
        + token["smart_money_score"] * 0.35
        + token["social_score"] * 0.15
        + token["narrative_score"] * 0.15
    )

    return round(confidence)