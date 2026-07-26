"""
AIE Token Normalizer

Converts every discovery source into one unified token model.
"""


def normalize_token(token):

    return {

        # ------------------------
        # Identity
        # ------------------------

        "source": token.get("source", "Unknown"),

        "ticker": (
            token.get("ticker")
            or token.get("symbol")
            or "UNKNOWN"
        ),

        "symbol": (
            token.get("symbol")
            or token.get("ticker")
            or "UNKNOWN"
        ),

        "name": (
            token.get("name")
            or token.get("ticker")
            or "UNKNOWN"
        ),

        "address": token.get("address", ""),

        # ------------------------
        # Market
        # ------------------------

        "price": float(token.get("price", 0)),

        "liquidity": float(token.get("liquidity", 0)),

        "volume": float(token.get("volume", 0)),

        # ------------------------
        # Launch
        # ------------------------

        "created_at": token.get("created_at"),

        "age_minutes": float(
            token.get("age_minutes", 999)
        ),

        "dex": token.get("dex", "unknown"),

        # ------------------------
        # Discovery
        # ------------------------

        "discovery_score": float(
            token.get("discovery_score", 0)
        ),

        "rating": token.get("rating", ""),

    }