import time
import httpx

URL = "https://api.dexscreener.com/token-profiles/latest/v1"


def discover_new_pairs():

    print("=" * 60)
    print("DISCOVERY ENGINE")
    print("=" * 60)

    try:

        response = httpx.get(
            URL,
            timeout=20
        )

    except Exception as e:

        print("Connection Error:", e)
        return []

    print("Status:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        return []

    pairs = response.json()

    print(f"Found {len(pairs)} pairs")

    NOW = int(time.time() * 1000)

    MAX_AGE = 6 * 60 * 60 * 1000      # 6 hours

    MIN_LIQUIDITY = 5_000
    MAX_LIQUIDITY = 150_000

    MIN_VOLUME = 5_000

    filtered = []

    for pair in pairs:

        created = pair.get("pairCreatedAt")

        if created is None:
            continue

        age = NOW - created

        if age > MAX_AGE:
            continue

        liquidity = (
            pair.get("liquidity", {})
            .get("usd", 0)
        )

        volume = (
            pair.get("volume", {})
            .get("h24", 0)
        )

        if liquidity < MIN_LIQUIDITY:
            continue

        if liquidity > MAX_LIQUIDITY:
            continue

        if volume < MIN_VOLUME:
            continue

        base = pair.get("baseToken", {})

        candidate = {

            "ticker": base.get("symbol"),

            "name": base.get("name"),

            "address": base.get("address"),

            "price": pair.get("priceUsd"),

            "liquidity": liquidity,

            "volume": volume,

            "dex": pair.get("dexId"),

            "pair_created": created,

            "age_minutes": round(age / 60000, 1),

        }

        score = 0

        if liquidity > 10000:
            score += 20

        if liquidity > 25000:
            score += 20

        if volume > liquidity:
            score += 20

        if volume > liquidity * 2:
            score += 20

        if age < 60 * 60 * 1000:
            score += 20

        candidate["launch_score"] = min(score, 100)

        filtered.append(candidate)

    filtered = sorted(
        filtered,
        key=lambda x: x["launch_score"],
        reverse=True,
    )

    return filtered