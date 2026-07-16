import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")

BIRDEYE_URL = "https://public-api.birdeye.so/defi/tokenlist"


def get_birdeye_data():

    headers = {
        "X-API-KEY": API_KEY
    }

    response = httpx.get(
        BIRDEYE_URL,
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("data", [])