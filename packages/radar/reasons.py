def get_reasons(token):

    reasons = []

    if token.get("liquidity", 0) >= 500000:
        reasons.append("High Liquidity")

    if token.get("volume", 0) >= 500000:
        reasons.append("High Trading Volume")

    if token.get("community_score", 0) >= 50:
        reasons.append("Strong Community")

    if token.get("smart_money_score", 0) >= 40:
        reasons.append("Smart Money Activity")

    if token.get("social_score", 0) >= 70:
        reasons.append("Trending Socials")

    if token.get("narrative_score", 0) >= 60:
        reasons.append("Strong Narrative")

    if token.get("source") == "Birdeye":
        reasons.append("Trusted Source")

    if len(reasons) == 0:
        reasons.append("General Market Activity")

    return reasons