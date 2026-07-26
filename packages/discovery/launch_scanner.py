import httpx
import time

DEX_URL = "https://api.dexscreener.com/latest/dex/search?q=solana"

# Tokens we NEVER want
BLACKLIST = {
    "SOL",
    "USDC",
    "USDT",
    "JUP",
    "JTO",
    "BONK",
    "WBTC",
    "ETH",
}


def discover_launches():

    print("=" * 60)
    print("🦅 HAWK LAUNCH SCANNER")
    print("=" * 60)

    response = httpx.get(
        DEX_URL,
        timeout=20,
    )

    if response.status_code != 200:
        print(response.text)
        return []

    pairs = response.json().get("pairs", [])

    now = int(time.time() * 1000)

    launches = []

    for pair in pairs:

        base = pair.get("baseToken", {})

        symbol = base.get("symbol")

        if symbol in BLACKLIST:
            continue

        created = pair.get("pairCreatedAt")

        if created is None:
            continue

        age_minutes = (now - created) / 60000

        liquidity = (
            pair.get("liquidity", {})
            .get("usd", 0)
        )

        volume = (
            pair.get("volume", {})
            .get("h24", 0)
        )

        # ---------------------
        # FILTERS
        # ---------------------

        if age_minutes > 360:
            continue

        if liquidity < 10000:
            continue

        if liquidity > 250000:
            continue

        launches.append({

            "ticker": symbol,

            "name": base.get("name"),

            "address": base.get("address"),

            "price": pair.get("priceUsd"),

            "liquidity": liquidity,

            "volume": volume,

            "age_minutes": round(age_minutes, 1),

            "dex": pair.get("dexId"),

        })

    launches.sort(
        key=lambda x: x["age_minutes"]
    )

    return launches