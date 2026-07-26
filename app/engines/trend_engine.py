from dataclasses import dataclass

from packages.database.database import (
    get_token,
    save_token,
)


@dataclass
class TrendResult:

    score: int
    reasons: list[str]


class TrendEngine:

    def analyze(self, token: dict) -> TrendResult:

        score = 50
        reasons = []

        previous = get_token(token["address"])

        if previous is None:

            reasons.append("First observation")

        else:

            previous_alpha = previous.get("alpha", 0)
            current_alpha = token.get("alpha", 0)

            if current_alpha > previous_alpha:

                score += 20
                reasons.append("Alpha improving")

            elif current_alpha < previous_alpha:

                score -= 20
                reasons.append("Alpha weakening")

            previous_volume = previous.get("volume_24h", 0)
            current_volume = token.get("volume_24h", 0)

            if current_volume > previous_volume:

                score += 15
                reasons.append("Volume increasing")

            elif current_volume < previous_volume:

                score -= 10
                reasons.append("Volume decreasing")

            previous_liquidity = previous.get("liquidity_usd", 0)
            current_liquidity = token.get("liquidity_usd", 0)

            if current_liquidity > previous_liquidity:

                score += 10
                reasons.append("Liquidity improving")

        save_token(token)

        score = max(0, min(score, 100))

        return TrendResult(
            score=score,
            reasons=reasons,
        )