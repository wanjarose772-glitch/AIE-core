import requests


BASE_URL = "https://api.dexscreener.com/latest/dex/search"


class DexScreenerCollector:

    def search(self, query: str):

        url = f"{BASE_URL}?q={query}"

        response = requests.get(
            url,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("pairs", [])