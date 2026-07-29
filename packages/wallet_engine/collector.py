"""
AIE Wallet Collector
"""

import json
import httpx

from packages.config.settings import BIRDEYE_API_KEY

URL = "https://public-api.birdeye.so/defi/v3/token/holder"


def collect_wallets(address):

    if not BIRDEYE_API_KEY:
        print("NO BIRDEYE API KEY")
        return []

    # ---------------------------------
    # Clean mint address
    # ---------------------------------

    address = str(address).strip()

    if address.startswith("solana_"):
        address = address.replace("solana_", "", 1)

    print("\n============================")
    print("WALLET ENGINE")
    print("============================")
    print("Mint:", address)

    headers = {
        "X-API-KEY": BIRDEYE_API_KEY,
        "x-chain": "solana",
        "accept": "application/json",
    }

    params = {
        "address": address,
        "offset": 0,
        "limit": 20,
    }

    try:

        response = httpx.get(
            URL,
            headers=headers,
            params=params,
            timeout=20,
        )

        print("Status:", response.status_code)

        try:
            print(json.dumps(response.json(), indent=2))
        except Exception:
            print(response.text)

        if response.status_code != 200:
            return []

        body = response.json()

        holders = body.get("data", {}).get("items", [])

        wallets = []

        # ---------------------------------
        # Total holder amount
        # ---------------------------------

        total_amount = sum(
            float(holder.get("ui_amount", 0))
            for holder in holders
        )

        print(f"TOTAL HOLDER AMOUNT: {total_amount}")

        # ---------------------------------
        # Build wallet list
        # ---------------------------------

        for holder in holders:

            amount = float(holder.get("ui_amount", 0))

            if total_amount > 0:
                percentage = (amount / total_amount) * 100
            else:
                percentage = 0

            wallets.append(
                {
                    "address": holder.get("owner"),
                    "amount": amount,
                    "percentage": round(percentage, 2),
                }
            )

        print(f"Wallets Found: {len(wallets)}")

        return wallets

    except Exception as e:

        print("Wallet Collector Error")
        print(e)

        return []