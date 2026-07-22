import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"


def collect_wallet_data(token_address):

    print("=" * 60)
    print("HELIUS COLLECTOR RUNNING")
    print("TOKEN:", token_address)
    print("=" * 60)

    payload = {
        "jsonrpc": "2.0",
        "id": "holders",
        "method": "getTokenLargestAccounts",
        "params": [token_address],
    }

    try:

        response = httpx.post(
            URL,
            json=payload,
            timeout=20,
        )

        print("Helius Status:", response.status_code)

        data = response.json()

        if "result" not in data:
            print("Helius returned no result.")
            print(data)
            return None

        holders = data["result"]["value"]

        print("Largest wallets:", len(holders))

        return {
            "holder": len(holders),
            "largest_wallets": holders,
        }

    except Exception as e:

        print("HELIUS ERROR")
        print(e)

        return None