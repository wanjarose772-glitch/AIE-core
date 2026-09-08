"""
AIE Holder Quality Engine
"""


class HolderEngine:

    def analyze(self, token):

        wallets = token.get("wallets", [])

        if not wallets:
            token["holder_score"] = 0
            token["holder_rating"] = "POOR"
            return token

        largest = max(
            wallet.get("percentage", 0)
            for wallet in wallets
        )

        score = 100

        # Penalize concentration

        if largest > 50:
            score -= 70

        elif largest > 30:
            score -= 40

        elif largest > 20:
            score -= 20

        # Reward decentralization

        if len(wallets) >= 20:
            score += 10

        score = max(0, min(score, 100))

        token["holder_score"] = score

        if score >= 80:
            token["holder_rating"] = "EXCELLENT"

        elif score >= 60:
            token["holder_rating"] = "GOOD"

        elif score >= 40:
            token["holder_rating"] = "AVERAGE"

        else:
            token["holder_rating"] = "POOR"

        return token