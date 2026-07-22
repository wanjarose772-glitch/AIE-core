import os
import httpx
from dotenv import load_dotenv

load_dotenv()

print("USING BIRDEYE FILE:", __file__)

API_KEY = os.getenv("BIRDEYE_API_KEY")

TOKEN_LIST_URL = "https://public-api.birdeye.so/defi/tokenlist"
TOKEN_OVERVIEW_URL = "https://public-api.birdeye.so/defi/token_overview"

HEADERS = {
    "X-API-KEY": API_KEY
}


def get_trending_tokens():
    """
    Returns the current trending tokens from Birdeye.
    """

    print("\n===== BIRDEYE DEBUG =====")
    print("API KEY FOUND:", API_KEY is not None)

    if API_KEY:
        print("FIRST 8 CHARS:", API_KEY[:8])

    try:

        response = httpx.get(
            TOKEN_LIST_URL,
            headers=HEADERS,
            timeout=20
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return []

        data = response.json()

        tokens = (
            data.get("data", {})
                .get("tokens", [])
        )

        print(f"Downloaded {len(tokens)} tokens.")

        return tokens

    except Exception as e:

        print("=" * 60)
        print("BIRDEYE TOKEN LIST ERROR")
        print(e)
        print("=" * 60)

        return []


def get_token_overview(address: str):
    """
    Returns metadata for a token.
    """

    print(f"\nFetching overview for {address}")

    try:

        response = httpx.get(
            TOKEN_OVERVIEW_URL,
            headers=HEADERS,
            params={
                "address": address
            },
            timeout=20
        )

        print("Overview Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return {}

        data = response.json()

        return data.get("data", {})

    except Exception as e:

        print("=" * 60)
        print("TOKEN OVERVIEW ERROR")
        print(address)
        print(e)
        print("=" * 60)

        return {}


# Backwards compatibility
get_birdeye_data = get_trending_tokens