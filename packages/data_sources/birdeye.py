import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")

print("===== BIRDEYE DEBUG =====")
print("API KEY FOUND:", API_KEY is not None)
if API_KEY:
    print("FIRST 8 CHARS:", API_KEY[:8])
print("=========================")

BIRDEYE_URL = "https://public-api.birdeye.so/defi/tokenlist"


def get_birdeye_data():

    if not API_KEY:
        return []

    headers = {
        "X-API-KEY": API_KEY
    }

    response = httpx.get(
        BIRDEYE_URL,
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        print("Birdeye Error:", response.status_code)
        print(response.text)
        return []

    data = response.json()

    return data.get("data", [])