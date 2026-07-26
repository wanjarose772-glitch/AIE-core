class BirdEyeNormalizer:

    def normalize(self, token):

        return {

            "symbol": token["symbol"],

            "name": token["name"],

            "address": token["address"],

            "liquidity_usd": token["liquidity"],

            "market_cap": token["marketcap"],

            "volume_24h": token["volume24hUSD"],

            "holders": 0,

            "buys": 0,

            "sells": 0,

            "price": token["price"],

            "rank": token["rank"],

        }