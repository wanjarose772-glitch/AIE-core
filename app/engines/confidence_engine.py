from dataclasses import dataclass


@dataclass
class ConfidenceResult:
    score: int
    reasons: list[str]


class ConfidenceEngine:

    def analyze(
        self,
        token: dict,
        alpha,
        risk,
    ) -> ConfidenceResult:

        confidence = 100
        reasons = []

        required_fields = [
            "liquidity_usd",
            "market_cap",
            "holders",
            "volume_24h",
            "buys",
            "sells",
        ]

        for field in required_fields:

            if token.get(field) is None:

                confidence -= 15
                reasons.append(f"Missing {field}")

        if token.get("holders", 0) < 100:

            confidence -= 10
            reasons.append("Very low holder count")

        if token.get("volume_24h", 0) < 5000:

            confidence -= 10
            reasons.append("Low trading activity")

        # Confidence drops if alpha is weak

        if alpha.score < 50:

            confidence -= 15
            reasons.append("Weak alpha score")

        # Confidence drops if risk is high

        if risk.level == "HIGH":

            confidence -= 25
            reasons.append("High project risk")

        elif risk.level == "MEDIUM":

            confidence -= 10
            reasons.append("Moderate project risk")

        confidence = max(0, min(100, confidence))

        return ConfidenceResult(
            score=confidence,
            reasons=reasons,
        )