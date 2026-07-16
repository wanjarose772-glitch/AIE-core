from packages.decision.reasons import build_reasons
from packages.decision.risk import calculate_risk


def make_decision(token):

    reasons = build_reasons(token)

    risk = calculate_risk(token)

    if token["alpha_score"] >= 90 and token["confidence"] >= 50:

        decision = "🟢 BUY"

    elif token["alpha_score"] >= 75:

        decision = "👀 WATCH"

    else:

        decision = "🔴 PASS"

    return {

        "decision": decision,

        "risk": risk,

        "reasons": reasons

    }