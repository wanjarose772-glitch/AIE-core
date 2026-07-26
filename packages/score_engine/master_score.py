class MasterScoreEngine:

    def calculate(self, analysis):

        score = 0

        # -------------------------
        # Discovery
        # -------------------------

        discovery = analysis.get("discovery_score", 0)
        score += discovery * 0.20

        # -------------------------
        # Alpha
        # -------------------------

        alpha = analysis.get("alpha_score", 0)
        score += alpha * 0.25

        # -------------------------
        # Momentum
        # -------------------------

        momentum = analysis.get("momentum", 0)
        score += momentum * 0.15

        # -------------------------
        # Opportunity
        # -------------------------

        opportunity = analysis.get("opportunity", 0)
        score += opportunity * 0.10

        # -------------------------
        # Trend
        # -------------------------

        trend = analysis.get("trend", 0)
        score += trend * 0.10

        # -------------------------
        # Wallet Intelligence
        # -------------------------

        wallets = analysis.get("wallet_score", 0)
        score += wallets * 0.10

        # -------------------------
        # Whale Intelligence
        # -------------------------

        whales = analysis.get("whale_score", 0)
        score += whales * 0.10

        # -------------------------
        # Risk Penalty
        # -------------------------

        risk = analysis.get("risk_score", 0)
        score -= risk * 0.10

        score = round(max(0, min(score, 100)), 1)

        if score >= 90:
            rating = "ASILI PRIME"
            recommendation = "STRONG BUY"

        elif score >= 75:
            rating = "ASILI WATCH"
            recommendation = "BUY"

        elif score >= 60:
            rating = "SPECULATIVE"
            recommendation = "WATCH"

        else:
            rating = "REJECT"
            recommendation = "PASS"

        return {
            "aie_score": score,
            "rating": rating,
            "recommendation": recommendation,
        }