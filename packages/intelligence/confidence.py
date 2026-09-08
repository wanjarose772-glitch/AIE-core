"""
AIE Confidence Engine

Combines every intelligence engine
into one final AIE score.
"""


def compute_confidence(token):

    # Missing enrichment is unknown, not a failed signal.  Average only the
    # scores the current pipeline actually produced.
    signals = [
        token.get("alpha_score"), token.get("discovery_score"),
        token.get("wallet_score"), token.get("whale_score"),
        token.get("momentum"), token.get("opportunity"),
        token.get("trend"), token.get("social_score"),
    ]
    available = [float(signal) for signal in signals if signal is not None]
    score = sum(available) / len(available) if available else 0
    score -= float(token.get("risk_score") or 0) * 0.20

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
