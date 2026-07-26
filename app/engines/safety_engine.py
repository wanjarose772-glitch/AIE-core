from dataclasses import dataclass


@dataclass
class SafetyResult:
    score: int
    level: str
    reasons: list


class SafetyEngine:

    def analyze(self, token):

        score = 100
        reasons = []

        liquidity = token.get("liquidity_usd", 0)

        if liquidity < 25_000:
            score -= 60
            reasons.append("Very low liquidity")

        elif liquidity < 100_000:
            score -= 30
            reasons.append("Low liquidity")

        elif liquidity < 250_000:
            score -= 15
            reasons.append("Average liquidity")

        market_cap = token.get("market_cap", 0)

        if market_cap < 100_000:
            score -= 25
            reasons.append("Extremely small market cap")

        score = max(0, min(score, 100))

        if score >= 80:
            level = "LOW"

        elif score >= 60:
            level = "MEDIUM"

        else:
            level = "HIGH"

        return SafetyResult(
            score=score,
            level=level,
            reasons=reasons,
        )