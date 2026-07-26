from dataclasses import dataclass


@dataclass
class RecommendationResult:
    action: str
    summary: str


class RecommendationEngine:

    def analyze(self, alpha, safety):

        if safety.level == "HIGH":
            action = "AVOID"
            summary = "Risk is too high."

        elif alpha.score >= 85:
            action = "BUY"
            summary = "Strong opportunity."

        elif alpha.score >= 70:
            action = "WATCH"
            summary = "Promising but needs confirmation."

        else:
            action = "PASS"
            summary = "No clear edge."

        return RecommendationResult(
            action=action,
            summary=summary,
        )