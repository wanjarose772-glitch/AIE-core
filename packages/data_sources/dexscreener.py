import httpx


DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/search?q=solana"


def get_market_data():
    response = httpx.get(DEXSCREENER_URL, timeout=10)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("pairs", [])