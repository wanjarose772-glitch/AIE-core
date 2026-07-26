"""
Opportunity Engine
Measures upside potential.
"""

from dataclasses import dataclass


@dataclass
class OpportunityResult:
    score: int
    reasons: list


class OpportunityEngine:

    def analyze(self, token):

        score = 0
        reasons = []

        market_cap = token.get("market_cap", 0)
        liquidity = token.get("liquidity_usd", 0)

        if market_cap < 2000000:
            score += 40
            reasons.append("Very small market cap")

        elif market_cap < 10000000:
            score += 25
            reasons.append("Growth-stage market cap")

        if liquidity > 100000:
            score += 30
            reasons.append("Enough liquidity")

        volume = token.get("volume_24h", 0)

        if volume > liquidity:
            score += 30
            reasons.append("High capital turnover")

        return OpportunityResult(score, reasons)