def build_reasons(token):

    reasons = []

    if token["alpha_score"] >= 90:
        reasons.append("High Alpha Score")

    if token["momentum_score"] >= 60:
        reasons.append("Strong Momentum")

    if token["liquidity_change"] > 20:
        reasons.append("Growing Liquidity")

    if token["volume_change"] > 20:
        reasons.append("Heavy Trading Volume")

    if token["social_score"] >= 70:
        reasons.append("Trending Social Activity")

    if token["smart_money_score"] >= 20:
        reasons.append("Smart Wallet Interest")

    if token["community_score"] >= 20:
        reasons.append("Strong Community")

    return reasons