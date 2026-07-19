import requests

BASE_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"


def fetch_latest_pairs():

    """
    Returns the latest Solana trading pairs.
    """

    response = requests.get(BASE_URL, timeout=10)

    response.raise_for_status()

    data = response.json()

    return data.get("pairs", [])