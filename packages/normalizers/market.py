def normalize_pair(pair):
    """
    Convert a DexScreener trading pair into AIE's internal format.
    """

    return {
        "ticker": pair.get("baseToken", {}).get("symbol", "UNKNOWN"),
        "name": pair.get("baseToken", {}).get("name", "Unknown"),
        "chain": pair.get("chainId", "Unknown"),
        "price": float(pair.get("priceUsd", 0) or 0),
        "liquidity": pair.get("liquidity", {}).get("usd", 0),
        "volume": pair.get("volume", {}).get("h24", 0),
        "market_cap": pair.get("marketCap", 0),
        "dex": pair.get("dexId", "Unknown"),
        "pair_address": pair.get("pairAddress", ""),
        "source": "DexScreener"
    }