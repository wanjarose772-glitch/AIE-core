"""
AIE Conviction Engine
"""


def compute_conviction(token):

    score = 0

    # ---------------------------------
    # Discovery (30%)
    # ---------------------------------

    score += token.get("discovery_score", 0) * 0.30

    # ---------------------------------
    # Wallets (25%)
    # ---------------------------------

    score += token.get("wallet_score", 0) * 0.25

    # ---------------------------------
    # Holder Quality (20%)
    # ---------------------------------

    score += token.get("holder_score", 0) * 0.20

    # ---------------------------------
    # Liquidity (15%)
    # ---------------------------------

    score += token.get("liquidity_score", 0) * 0.15

    # ---------------------------------
    # Momentum (10%)
    # ---------------------------------

    score += token.get("momentum_score", 0) * 0.10

    score = round(score, 2)

    token["conviction"] = score

    if score >= 85:
        token["recommendation"] = "BUY"

    elif score >= 70:
        token["recommendation"] = "WATCH"

    else:
        token["recommendation"] = "PASS"

    return token