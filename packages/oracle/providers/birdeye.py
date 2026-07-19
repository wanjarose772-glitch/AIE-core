import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")


def get_token_overview(address):

    url = "https://public-api.birdeye.so/defi/token_overview"

    headers = {
        "X-API-KEY": API_KEY,
        "x-chain": "solana"
    }

    params = {
        "address": address
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return response.json().get("data", {})