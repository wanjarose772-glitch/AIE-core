def calculate_risk(token):

    risk = 0

    if token["liquidity"] < 100000:
        risk += 1

    if token["community_score"] == 0:
        risk += 1

    if token["social_score"] < 20:
        risk += 1

    if token["smart_wallets"] == 0:
        risk += 1

    if risk >= 3:
        return "High"

    elif risk == 2:
        return "Medium"

    return "Low"