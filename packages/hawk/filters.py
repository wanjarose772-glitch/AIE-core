"""
Safety Filters

Version 0.1

Currently accepts every token.

Later this module will remove
rug pulls and unsafe launches.
"""


EXCLUDED_SYMBOLS = {
    "SOL", "USDC", "USDT", "BTC", "ETH", "WETH", "WBTC", "AAPL",
    "NVDA", "META", "HOOD", "OPENAI", "CBBTC",
}

SUSPICIOUS_TERMS = ("airdrop", "claim", "presale", "test", "v2", "1000x")


def safety_filter(tokens):
    """Keep only liquid, tradeable early-launch candidates.

    These are conservative noise/risk gates, not proof a token is safe.
    Contract permissions, holder concentration, and deployer history must be
    added as provider data becomes available.
    """
    accepted = []
    seen_addresses = set()

    for token in tokens:
        symbol = (token.get("ticker") or "").strip().upper()
        name = (token.get("name") or "").strip().lower()
        address = token.get("address") or ""
        liquidity = float(token.get("liquidity") or 0)
        volume = float(token.get("volume") or 0)
        market_cap = float(token.get("market_cap") or 0)

        if not symbol or symbol in EXCLUDED_SYMBOLS or address in seen_addresses:
            continue
        if any(term in name or term in symbol.lower() for term in SUSPICIOUS_TERMS):
            continue
        # Insufficient liquidity makes price and volume signals too easy to
        # manipulate; overly large caps are no longer early-launch candidates.
        if not 10_000 <= liquidity <= 300_000:
            continue
        if volume < 5_000 or not 25_000 <= market_cap <= 10_000_000:
            continue
        # Extreme volume relative to liquidity is commonly wash activity.
        if volume / liquidity > 12:
            continue

        token["risk_flags"] = []
        token["screening_status"] = "PASSED INITIAL SCREEN"
        accepted.append(token)
        seen_addresses.add(address)

    return accepted
