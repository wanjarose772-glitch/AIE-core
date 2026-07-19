from packages.hawk.sources.birdeye import fetch_new_tokens


def fetch_new_launches():

    tokens = fetch_new_tokens()

    launches = []

    for token in tokens:

        launches.append({

            "ticker": token.get("symbol", "UNKNOWN"),

            "name": token.get("name", ""),

            "price": token.get("price", 0),

            "market_cap": token.get("market_cap", 0),

            "liquidity": token.get("liquidity", 0),

            "volume": token.get("volume_24h", 0),

            "address": token.get("address", ""),

            "logo": token.get("logo_uri", ""),

            "created_at": token.get("listed_at", 0)

        })

    launches.sort(

        key=lambda x: x["created_at"] or 0,

        reverse=True

    )

    return launches