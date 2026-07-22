from packages.config.settings import (
    HIGH_LIQUIDITY,
    MEDIUM_LIQUIDITY,
    HIGH_VOLUME,
    MEDIUM_VOLUME,
    TRUSTED_DEXES,
)


def calculate_alpha_score(token):
    """
    Calculate Alpha Score.
    Missing values automatically become 0.
    """

    score = 0

    # ----------------------
    # Liquidity
    # ----------------------

    liquidity = token.get("liquidity") or 0

    if liquidity >= HIGH_LIQUIDITY:
        score += 30
    elif liquidity >= MEDIUM_LIQUIDITY:
        score += 20
    elif liquidity >= 25_000:
        score += 10

    # ----------------------
    # Volume
    # ----------------------

    volume = token.get("volume") or 0

    if volume >= HIGH_VOLUME:
        score += 25
    elif volume >= MEDIUM_VOLUME:
        score += 15
    elif volume >= 10_000:
        score += 8

    # ----------------------
    # Market Cap
    # ----------------------

    market_cap = token.get("market_cap") or 0

    if 100_000 <= market_cap <= 5_000_000:
        score += 25
    elif market_cap <= 20_000_000:
        score += 15

    # ----------------------
    # Trusted Source
    # ----------------------

    if token.get("source") == "Birdeye":
        score += 20
    elif token.get("dex") in TRUSTED_DEXES:
        score += 20

    return score