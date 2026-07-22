import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")

HEADERS = {
    "X-API-KEY": API_KEY
}

TRANSACTIONS_URL = "https://public-api.birdeye.so/defi/txs/token"


def get_token_transactions(address: str):

    params = {
        "address": address,
        "limit": 50
    }

    try:

        response = httpx.get(
            TRANSACTIONS_URL,
            headers=HEADERS,
            params=params,
            timeout=15
        )

        print(f"\nFetching transactions for {address}")
        print("Transaction Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return None

        data = response.json()

        return data.get("data", {})

    except Exception as e:

        print(f"Transaction error for {address}")
        print(e)

        return None