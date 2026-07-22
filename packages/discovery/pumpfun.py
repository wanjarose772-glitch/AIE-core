import httpx

PUMPFUN_URL = "https://frontend-api.pump.fun/coins"


def discover_new_launches(limit=20):

    print("=" * 60)
    print("PUMP.FUN DISCOVERY")
    print("=" * 60)

    try:
        response = httpx.get(
            PUMPFUN_URL,
            timeout=20
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return []

        coins = response.json()

        launches = []

        for coin in coins[:limit]:

            launches.append({

                "ticker": coin.get("symbol"),

                "name": coin.get("name"),

                "address": coin.get("mint"),

                "creator": coin.get("creator"),

                "market_cap": coin.get("market_cap"),

                "created": coin.get("created_timestamp"),

                "volume": coin.get("volume_24h"),

                "reply_count": coin.get("reply_count"),

                "image": coin.get("image_uri"),

            })

        print(f"Found {len(launches)} new launches.")

        return launches

    except Exception as e:

        print(e)

        return []