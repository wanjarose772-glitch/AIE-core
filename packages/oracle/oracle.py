"""
PROJECT ORACLE

The reasoning engine.

Turns market data into
human-readable intelligence.
"""


def build_reasoning(token):

    liquidity = float(token.get("liquidity") or 0)
    volume = float(token.get("volume") or 0)
    alpha = token.get("alpha_score", 0)

    reasons = []

    if liquidity >= 100000:
        reasons.append(
            "Healthy liquidity lowers immediate liquidity risk."
        )

    if volume >= 500000:
        reasons.append(
            "Strong trading volume suggests active market participation."
        )

    if alpha >= 90:
        reasons.append(
            "Token qualifies for ASILI PRIME based on current Alpha score."
        )

    if alpha >= 75:
        reasons.append(
            "Momentum is worth monitoring closely."
        )

    if len(reasons) == 0:
        reasons.append(
            "Insufficient signals. Continue monitoring."
        )

    return " ".join(reasons)