def calculate_confidence(token):

    confidence = 0

    # Alpha Score (40)
    confidence += min(token.get("alpha_score", 0) / 100 * 40, 40)

    # Narrative (15)
    confidence += min(token.get("narrative_score", 0), 15)

    # Community Metadata (15)
    confidence += min(token.get("community_score", 0) / 80 * 15, 15)

    # Smart Money (15)
    confidence += min(token.get("smart_money_score", 0), 15)

    # Social (15)
    confidence += min(token.get("social_score", 0) / 100 * 15, 15)

    return round(confidence)