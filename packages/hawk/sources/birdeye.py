import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")

URL = "https://public-api.birdeye.so/defi/v2/tokens/new_listing"


def fetch_new_tokens():

    headers = {
        "X-API-KEY": API_KEY,
        "x-chain": "solana"
    }

    params = {
        "limit": 20,
        "meme_platform_enabled": "true"
    }

    try:
        response = requests.get(
            URL,
            headers=headers,
            params=params,
            timeout=20
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        # A live-data provider being temporarily unavailable must not take the
        # dashboard down.  The UI can render an empty state and retry.
        print(f"Birdeye new-listings request failed: {error}")
        return []

    return data.get("data", {}).get("items", [])
