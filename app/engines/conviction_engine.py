from dataclasses import dataclass


@dataclass
class ConvictionResult:

    score: int
    level: str
    action: str
    reasons: list[str]


class ConvictionEngine:

    def analyze(
     self,
     alpha,
     momentum,
        opportunity,
        confidence,
        risk,
    ) -> ConvictionResult:

        score = 0
        reasons = []

        # --------------------
        # Alpha
        # --------------------

        score += alpha.score * 0.20

        if alpha.score >= 70:
            reasons.append("Strong alpha")

        elif alpha.score >= 50:
            reasons.append("Average alpha")

        else:
            reasons.append("Weak alpha")

        # --------------------
        # Momentum
        # --------------------

        score += momentum.score * 0.20

        if momentum.score >= 60:
            reasons.append("Momentum building")

        # --------------------
        # Opportunity
        # --------------------

        score += opportunity.score * 0.20

        if opportunity.score >= 70:
            reasons.append("Large upside potential")

        # --------------------
        # Confidence
        # --------------------

        score += confidence.score * 0.20

        if confidence.score >= 80:
            reasons.append("Reliable data")

        # --------------------
        # Risk
        # --------------------

        if risk.level == "LOW":

            score += 20
            reasons.append("Low risk")

        elif risk.level == "MEDIUM":

            score += 10
            reasons.append("Moderate risk")

        else:

            reasons.append("High risk")

        score = round(min(score, 100))

        if score >= 85:

            level = "VERY HIGH"
            action = "BUY"

        elif score >= 70:

            level = "HIGH"
            action = "WATCH"

        elif score >= 55:

            level = "MEDIUM"
            action = "PASS"

        else:

            level = "LOW"
            action = "AVOID"

        return ConvictionResult(
            score=score,
            level=level,
            action=action,
            reasons=reasons,
        )