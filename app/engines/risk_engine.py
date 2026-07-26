from dataclasses import dataclass

from app.config.scoring import (
    MIN_LIQUIDITY,
    MICRO_CAP,
    MIN_HOLDERS,
    MIN_VOLUME,
    MAX_SCORE,
    MIN_SCORE,
)


@dataclass
class RiskResult:
    score: int
    level: str
    reasons: list


class RiskEngine:

    def analyze(self, token: dict) -> RiskResult:

        score = MAX_SCORE
        reasons = []

        liquidity = token.get("liquidity_usd", 0)

        if liquidity < MIN_LIQUIDITY:
            score -= 30
            reasons.append("Liquidity below minimum threshold")

        market_cap = token.get("market_cap", 0)

        if market_cap < MICRO_CAP:
            score -= 10
            reasons.append("Micro-cap token")

        holders = token.get("holders", 0)

        if holders < MIN_HOLDERS:
            score -= 20
            reasons.append("Low holder count")

        volume = token.get("volume_24h", 0)

        if volume < MIN_VOLUME:
            score -= 15
            reasons.append("Low trading volume")

        buys = token.get("buys", 0)
        sells = token.get("sells", 0)

        if sells > buys:
            score -= 10
            reasons.append("Selling pressure exceeds buying")

        score = max(score, MIN_SCORE)

        if score >= 75:
            level = "LOW"

        elif score >= 50:
            level = "MEDIUM"

        else:
            level = "HIGH"

        return RiskResult(
            score=score,
            level=level,
            reasons=reasons,
        )