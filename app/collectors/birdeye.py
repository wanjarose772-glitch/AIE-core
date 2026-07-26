import os
import requests
from dotenv import load_dotenv

load_dotenv()


class BirdEyeCollector:

    BASE_URL = "https://public-api.birdeye.so"

    def __init__(self):
        self.api_key = os.getenv("BIRDEYE_API_KEY")

        if not self.api_key:
            raise ValueError("BIRDEYE_API_KEY not found in .env")

    def trending_tokens(self, limit=20):

        url = (
            f"{self.BASE_URL}/defi/token_trending"
            f"?sort_by=rank"
            f"&sort_type=asc"
            f"&offset=0"
            f"&limit={limit}"
        )

        headers = {
            "X-API-KEY": self.api_key,
            "accept": "application/json",
            "x-chain": "solana",
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            print("Response:")
            print(response.text)

        response.raise_for_status()

        return response.json()