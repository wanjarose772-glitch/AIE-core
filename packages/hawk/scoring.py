"""
ASILI Alpha Engine V3

Dynamic intelligence scoring.

Each token begins at 30 points.

Signals increase the score.

Final score determines:

- Confidence
- Rating
"""

def calculate_alpha(token):

    score = 30

    liquidity = float(token.get("liquidity") or 0)
    volume = float(token.get("volume") or 0)
    market_cap = float(token.get("market_cap") or 0)

    # -----------------------
    # Liquidity (30 pts)
    # -----------------------

    if liquidity >= 100000:
        score += 30

    elif liquidity >= 50000:
        score += 25

    elif liquidity >= 25000:
        score += 20

    elif liquidity >= 10000:
        score += 15

    elif liquidity >= 5000:
        score += 10

    elif liquidity >= 1000:
        score += 5

    # -----------------------
    # Volume (25 pts)
    # -----------------------

    if volume >= 1000000:
        score += 25

    elif volume >= 500000:
        score += 20

    elif volume >= 100000:
        score += 15

    elif volume >= 50000:
        score += 10

    elif volume >= 10000:
        score += 5

    # -----------------------
    # Market Cap (20 pts)
    # -----------------------

    if market_cap > 0:

        if market_cap <= 500000:
            score += 20

        elif market_cap <= 1000000:
            score += 15

        elif market_cap <= 5000000:
            score += 10

        elif market_cap <= 10000000:
            score += 5

    # -----------------------
    # Bonus
    # -----------------------

    if liquidity > volume and liquidity > 10000:
        score += 5

    score = max(0, min(score, 100))

    confidence = min(98, score + 2)

    if score >= 90:
        rating = "👑 ASILI PRIME"

    elif score >= 75:
        rating = "🔷 ASILI WATCH"

    elif score >= 60:
        rating = "⚡ ASILI SPECULATIVE"

    else:
        rating = "🚫 ASILI REJECT"

    return {

        "alpha_score": score,

        "confidence": confidence,

        "rating": rating

    }