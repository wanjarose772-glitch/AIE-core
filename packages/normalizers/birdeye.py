def normalize_birdeye_token(token):
    """
    Convert a Birdeye token into AIE's internal format.
    """

    return {
        "ticker": token.get("symbol", "UNKNOWN"),
        "name": token.get("name", "Unknown"),
        "chain": "solana",
        "price": float(token.get("price", 0) or 0),
        "liquidity": token.get("liquidity", 0),
        "volume": token.get("v24hUSD", 0),
        "market_cap": token.get("mc", 0),
        "address": token.get("address", ""),
        "source": "Birdeye"
    }