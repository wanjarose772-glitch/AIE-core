import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HELIUS_API_KEY")

URL = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"


def get_helius_metadata(address):

    payload = {
        "jsonrpc": "2.0",
        "id": "aie",
        "method": "getAsset",
        "params": {
            "id": address
        }
    }

    try:

        response = httpx.post(
            URL,
            json=payload,
            timeout=20,
        )

        if response.status_code != 200:
            return {}

        data = response.json()

        return data.get("result", {})

    except Exception as e:

        print("Helius Metadata Error")
        print(e)

        return {}