"""
Confidence Engine
-----------------

Produces a confidence percentage (0-100)
based on every signal collected by AIE.
"""


def calculate_confidence(token: dict):

    score = 0

    # --------------------------
    # Liquidity
    # --------------------------

    liquidity = token.get("liquidity", 0)

    if liquidity >= 50000:
        score += 20

    elif liquidity >= 25000:
        score += 15

    elif liquidity >= 10000:
        score += 10

    # --------------------------
    # Volume
    # --------------------------

    volume = token.get("volume", 0)

    if volume >= 100000:
        score += 20

    elif volume >= 50000:
        score += 15

    elif volume >= 10000:
        score += 10

    # --------------------------
    # Smart wallets
    # --------------------------

    smart_wallets = token.get("smart_wallets", 0)

    score += min(smart_wallets * 4, 20)

    # --------------------------
    # Holder concentration
    # --------------------------

    concentration = token.get(
        "top_holder_percent",
        100
    )

    if concentration <= 10:
        score += 20

    elif concentration <= 20:
        score += 15

    elif concentration <= 35:
        score += 8

    # --------------------------
    # Age
    # --------------------------

    age = token.get("age_minutes", 0)

    if 5 <= age <= 120:
        score += 10

    elif age < 5:
        score += 5

    return min(score, 100)