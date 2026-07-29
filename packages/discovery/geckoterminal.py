import httpx
import json

GECKO_URL = (
    "https://api.geckoterminal.com/api/v2/networks/solana/new_pools"
)


def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def discover_gecko_launches():

    print("=" * 80)
    print("GECKOTERMINAL")
    print("=" * 80)

    try:

        response = httpx.get(GECKO_URL, timeout=20)

        print("Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return []

        payload = response.json()

        pools = payload.get("data", [])
        included = payload.get("included", [])

        token_lookup = {}
        dex_lookup = {}

        for item in included:

            attrs = item.get("attributes", {})

            if item.get("type") == "token":
                token_lookup[item["id"]] = attrs

            elif item.get("type") == "dex":
                dex_lookup[item["id"]] = attrs

        launches = []

        for pool in pools:

            attrs = pool.get("attributes", {})
            rel = pool.get("relationships", {})

            base = rel.get("base_token", {}).get("data", {})
            dex = rel.get("dex", {}).get("data", {})

            token = token_lookup.get(base.get("id"), {})
            dex_data = dex_lookup.get(dex.get("id"), {})

            # -------------------------
            # FALLBACK USING POOL NAME
            # -------------------------

            pool_name = attrs.get("name", "")

            if "/" in pool_name:
                fallback_symbol = pool_name.split("/")[0].strip()
            else:
                fallback_symbol = "UNKNOWN"

            symbol = (
                token.get("symbol")
                or token.get("token_symbol")
                or fallback_symbol
            )

            name = (
                token.get("name")
                or fallback_symbol
            )

            address = (
                token.get("address")
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

                "market_cap": safe_float(
                    attrs.get("market_cap_usd")
                    or attrs.get("fdv_usd")
                ),

                "created_at": attrs.get(
                    "pool_created_at"
                ),

                "dex": (
                    dex_data.get("identifier")
                    or dex.get("id")
                    or "unknown"
                )

            })

        print(f"\nParsed {len(launches)} launches.\n")

        return launches

    except Exception as e:

        print("\nGECKOTERMINAL ERROR")
        print(e)

        return []