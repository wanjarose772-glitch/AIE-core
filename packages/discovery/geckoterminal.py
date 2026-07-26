import httpx

GECKO_URL = (
    "https://api.geckoterminal.com/api/v2/networks/solana/new_pools"
)


def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def discover_gecko_launches():

    print("=" * 60)
    print("GECKOTERMINAL")
    print("=" * 60)

    try:

        response = httpx.get(
            GECKO_URL,
            timeout=20,
        )

        print(f"Status: {response.status_code}")

        if response.status_code != 200:
            print(response.text)
            return []

        payload = response.json()

        pools = payload.get("data", [])
        included = payload.get("included", [])

        print(f"Pools Found: {len(pools)}")

        # -----------------------------------
        # Build lookup tables
        # -----------------------------------

        token_lookup = {}
        dex_lookup = {}

        for item in included:

            item_type = item.get("type")
            item_id = item.get("id")
            attrs = item.get("attributes", {})

            if item_type == "token":
                token_lookup[item_id] = attrs

            elif item_type == "dex":
                dex_lookup[item_id] = attrs

        launches = []

        # -----------------------------------
        # Parse every pool
        # -----------------------------------

        for pool in pools:

            attrs = pool.get("attributes", {})
            rel = pool.get("relationships", {})

            base = (
                rel.get("base_token", {})
                .get("data", {})
            )

            dex = (
                rel.get("dex", {})
                .get("data", {})
            )

            token = token_lookup.get(
                base.get("id"),
                {}
            )

            dex_data = dex_lookup.get(
                dex.get("id"),
                {}
            )

            symbol = (
                token.get("symbol")
                or token.get("token_symbol")
                or token.get("name")
                or "UNKNOWN"
            )

            name = (
                token.get("name")
                or token.get("token_name")
                or symbol
            )

            address = (
                token.get("address")
                or token.get("token_address")
                or base.get("id")
                or ""
            )

            launches.append({

                "source": "GeckoTerminal",

                "ticker": symbol,

                "symbol": symbol,

                "name": name,

                "address": address,

                "price": safe_float(
                    attrs.get("base_token_price_usd")
                ),

                "liquidity": safe_float(
                    attrs.get("reserve_in_usd")
                ),

                "volume": safe_float(
                    (attrs.get("volume_usd") or {}).get("h24")
                ),

                "created_at": attrs.get(
                    "pool_created_at"
                ),

                "dex": (
                    dex_data.get("identifier")
                    or dex.get("id")
                    or "unknown"
                ),

            })

        print(f"Parsed {len(launches)} launches.")

        return launches

    except Exception as e:

        print("GeckoTerminal Error")
        print(e)

        return []