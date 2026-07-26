class TokenNormalizer:

    def normalize(self, pair):

        return {

            "symbol": pair["baseToken"]["symbol"],

            "name": pair["baseToken"]["name"],

            "liquidity_usd": pair.get("liquidity", {}).get("usd", 0),

            "market_cap": pair.get("marketCap", 0),

            "volume_24h": pair.get("volume", {}).get("h24", 0),

            "buys": pair.get("txns", {}).get("h24", {}).get("buys", 0),

            "sells": pair.get("txns", {}).get("h24", {}).get("sells", 0),

            # DexScreener doesn't reliably provide holder count.
            # BirdEye will enrich this later.
            "holders": 0,
        }