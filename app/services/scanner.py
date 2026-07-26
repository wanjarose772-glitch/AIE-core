from app.collectors.birdeye import BirdEyeCollector


class MarketScanner:

    def __init__(self):

        self.collector = BirdEyeCollector()

    def scan(self):

        data = self.collector.trending_tokens(20)

        tokens = []

        for coin in data["data"]["tokens"]:

            token = {
                "symbol": coin.get("symbol"),
                "name": coin.get("name"),
                "address": coin.get("address"),

                "liquidity_usd": coin.get("liquidity", 0),

                "market_cap": coin.get("marketcap", 0),

                "volume_24h": coin.get("volume24hUSD", 0),

                "holders": coin.get("holders", 0),

                "buys": coin.get("buys", 0),

                "sells": coin.get("sells", 0),

                "price": coin.get("price", 0),

                "rank": coin.get("rank", 0),

                # Placeholder until live whale data
                "whales": [],
            }

            tokens.append(token)

        return tokens