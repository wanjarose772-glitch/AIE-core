import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BIRDEYE_API_KEY")

URL = "https://public-api.birdeye.so/defi/token_overview"

HEADERS = {
    "X-API-KEY": API_KEY
}


def get_birdeye_metadata(address):

    try:

        response = httpx.get(
            URL,
            headers=HEADERS,
            params={
                "address": address
            },
            timeout=20,
        )

        if response.status_code != 200:
            return {}

        payload = response.json()

        return payload.get("data", {})

    except Exception as e:

        print("Birdeye Metadata Error")
        print(e)

        return {}