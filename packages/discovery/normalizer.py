"""
AIE Token Normalizer

Converts every discovery source into one unified token model.
"""


def normalize_token(token):

    ticker = (
        token.get("ticker")
        or token.get("symbol")
        or token.get("base_symbol")
        or ""
    )

    name = (
        token.get("name")
        or token.get("base_name")
        or ticker
    )

    # ---------------------------------
    # Clean Solana address
    # ---------------------------------

    address = token.get("address", "")

    if isinstance(address, str):
        address = address.removeprefix("solana_")

    return {

        # ------------------------
        # Identity
        # ------------------------

        "source": token.get("source", "Unknown"),

        "ticker": ticker if ticker else "UNKNOWN",

        "symbol": ticker if ticker else "UNKNOWN",

        "name": name if name else "UNKNOWN",

        "address": address,

        # ------------------------
        # Market
        # ------------------------

        "price": float(token.get("price", 0) or 0),

        "liquidity": float(token.get("liquidity", 0) or 0),

        "volume": float(token.get("volume", 0) or 0),

        "market_cap": float(token.get("market_cap", 0) or 0),

        # ------------------------
        # Launch
        # ------------------------

        "created_at": token.get("created_at"),

        "age_minutes": float(
            token.get("age_minutes", 999) or 999
        ),

        "dex": token.get("dex", "unknown"),

        # ------------------------
        # Discovery
        # ------------------------

        "discovery_score": float(
            token.get("discovery_score", 0)
        ),

        "rating": token.get("rating", ""),

        # ------------------------
        # Intelligence
        # ------------------------

        "wallets": [],
        "whales": [],

        "logo": None,
        "fdv": 0,
        "decimals": None,
        "verified": False,

        "wallet_score": 0,
        "wallet_rating": "POOR",

        "alpha_score": 0,
        "whale_score": 0,

        "momentum": 0,
        "opportunity": 0,
        "trend": 0,

        "risk_score": 0,

        "aie_score": 0,

        "recommendation": "UNKNOWN",
    }