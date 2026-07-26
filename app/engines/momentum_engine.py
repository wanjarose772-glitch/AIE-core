"""
Momentum Engine
Measures whether buying pressure is increasing.
"""

from dataclasses import dataclass


@dataclass
class MomentumResult:
    score: int
    reasons: list


class MomentumEngine:

    def analyze(self, token):

        score = 0
        reasons = []

        buys = token.get("buys", 0)
        sells = token.get("sells", 0)
        volume = token.get("volume_24h", 0)

        if buys > sells:
            score += 30
            reasons.append("Buy pressure exceeds sell pressure")

        if volume > 500000:
            score += 30
            reasons.append("Strong trading volume")

        if token.get("liquidity_usd", 0) > 100000:
            score += 20
            reasons.append("Healthy liquidity")

        if token.get("market_cap", 0) < 10000000:
            score += 20
            reasons.append("Early market cap")

        return MomentumResult(score, reasons)