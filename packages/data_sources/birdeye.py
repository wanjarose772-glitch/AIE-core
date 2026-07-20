import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")

BIRDEYE_URL = "https://public-api.birdeye.so/defi/tokenlist"


def get_birdeye_data():

    print("===== BIRDEYE DEBUG =====")
    print("API KEY FOUND:", API_KEY is not None)
    print("FIRST 8 CHARS:", API_KEY[:8] if API_KEY else "NONE")
    print("=========================")

    headers = {
        "X-API-KEY": API_KEY
    }

    response = httpx.get(
        BIRDEYE_URL,
        headers=headers,
        timeout=15
    )

    print("Status:", response.status_code)
    print("Response:", response.text[:500])

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("data", [])