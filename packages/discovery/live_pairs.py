import httpx
import time

DEX_URL = "https://api.dexscreener.com/latest/dex/search?q=SOL"


def discover_live_pairs():

    print("=" * 60)
    print("LIVE PAIR DISCOVERY")
    print("=" * 60)

    try:
        response = httpx.get(
            DEX_URL,
            timeout=20
        )

    except Exception as e:
        print("Request failed:", e)
        return []

    if response.status_code != 200:
        print("Status:", response.status_code)
        print(response.text)
        return []

    data = response.json()

    pairs = data.get("pairs", [])

    print(f"Downloaded {len(pairs)} pairs")

    now = int(time.time() * 1000)

    candidates = []

    print("\nEvaluating pairs...\n")

    for pair in pairs:

        created = pair.get("pairCreatedAt")

        liquidity = (
            pair.get("liquidity", {})
            .get("usd", 0)
        )

        volume = (
            pair.get("volume", {})
            .get("h24", 0)
        )

        base = pair.get("baseToken", {})

        if created:
            age = round((now - created) / 60000, 2)
        else:
            age = None

        print(
            f"{base.get('symbol')} | "
            f"Liquidity=${liquidity:,.0f} | "
            f"Age={age} mins | "
            f"Volume=${volume:,.0f}"
        )

        # Ignore pairs with no creation time
        if age is None:
            continue

        # Early-launch filters
        if liquidity < 5000:
            continue

        if liquidity > 200000:
            continue

        if age > 360:
            continue

        candidates.append({

            "ticker": base.get("symbol"),

            "name": base.get("name"),

            "address": base.get("address"),

            "price": pair.get("priceUsd"),

            "liquidity": liquidity,

            "volume": volume,

            "dex": pair.get("dexId"),

            "pair_created": created,

            "age_minutes": age,

        })

    candidates.sort(
        key=lambda x: x["liquidity"],
        reverse=True
    )

    return candidates