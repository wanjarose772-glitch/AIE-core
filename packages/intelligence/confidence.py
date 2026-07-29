"""
AIE Confidence Engine

Combines every intelligence engine
into one final AIE score.
"""


def compute_confidence(token):

    discovery = token.get("discovery_score", 0)
    wallet = token.get("wallet_score", 0)
    whale = token.get("whale_score", 0)
    momentum = token.get("momentum", 0)
    opportunity = token.get("opportunity", 0)
    trend = token.get("trend", 0)
    risk = token.get("risk_score", 0)

    score = (
        discovery * 0.25 +
        wallet * 0.20 +
        whale * 0.15 +
        momentum * 0.15 +
        opportunity * 0.15 +
        trend * 0.10
    )

    score -= risk * 0.20

    score = max(0, min(score, 100))

    token["aie_score"] = round(score, 1)

    if score >= 90:
        token["recommendation"] = "STRONG BUY"

    elif score >= 75:
        token["recommendation"] = "BUY"

    elif score >= 60:
        token["recommendation"] = "WATCH"

    elif score >= 40:
        token["recommendation"] = "SPECULATIVE"

    else:
        token["recommendation"] = "PASS"

    return token