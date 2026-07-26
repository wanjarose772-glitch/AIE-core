from types import SimpleNamespace


class AlphaEngine:

    def analyze(self, token):

        score = 0

        liquidity = float(token.get("liquidity", 0))
        volume = float(token.get("volume", 0))
        discovery = float(token.get("discovery_score", 0))
        age = float(token.get("age_minutes", 999))

        # -------------------------
        # Liquidity
        # -------------------------

        if liquidity >= 10000:
            score += 20
        elif liquidity >= 5000:
            score += 15
        elif liquidity >= 2000:
            score += 10

        # -------------------------
        # Volume
        # -------------------------

        if volume >= 100000:
            score += 25
        elif volume >= 50000:
            score += 20
        elif volume >= 10000:
            score += 15
        elif volume >= 2000:
            score += 10

        # -------------------------
        # Discovery Engine
        # -------------------------

        score += discovery * 0.20

        # -------------------------
        # Early Launch Bonus
        # -------------------------

        if age <= 5:
            score += 15
        elif age <= 15:
            score += 10
        elif age <= 30:
            score += 5

        score = round(min(score, 100), 1)

        return SimpleNamespace(score=score)