"""
Final AIE Decision Engine
"""


class DecisionEngine:

    @staticmethod
    def explain(token):

        reasons = []

        if token.get("discovery_score", 0) >= 80:
            reasons.append("Excellent early discovery")

        if token.get("wallet_score", 0) >= 70:
            reasons.append("Strong smart wallet activity")

        if token.get("whale_score", 0) >= 70:
            reasons.append("Whales accumulating")

        if token.get("momentum", 0) >= 60:
            reasons.append("Positive momentum")

        if token.get("risk_score", 0) <= 20:
            reasons.append("Low risk")

        return reasons