from packages.config.settings import (
    HIGH_LIQUIDITY,
    MEDIUM_LIQUIDITY,
    HIGH_VOLUME,
    MEDIUM_VOLUME,
    TRUSTED_DEXES,
)


def calculate_alpha_score(token):
    """
    Calculate an Alpha Score using normalized market data.
    """

    score = 0

    # Liquidity (30 points)
    liquidity = token.get("liquidity", 0)

    if liquidity >= HIGH_LIQUIDITY:
        score += 30
    elif liquidity >= MEDIUM_LIQUIDITY:
        score += 20
    elif liquidity >= 25_000:
        score += 10

    # Volume (25 points)
    volume = token.get("volume", 0)

    if volume >= HIGH_VOLUME:
        score += 25
    elif volume >= MEDIUM_VOLUME:
        score += 15
    elif volume >= 10_000:
        score += 8

    # Market Cap (25 points)
    market_cap = token.get("market_cap", 0)

    if 100_000 <= market_cap <= 5_000_000:
        score += 25
    elif market_cap <= 20_000_000:
        score += 15

    # Trusted DEX (20 points)
    if token.get("source") == "Birdeye":
        score += 20
    elif token.get("dex") in TRUSTED_DEXES:
        score += 20

    return score