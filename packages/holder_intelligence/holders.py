import httpx

from packages.config import HELIUS_API_KEY


def get_token_holders(token_address: str):

    url = (
        f"https://mainnet.helius-rpc.com/"
        f"?api-key={HELIUS_API_KEY}"
    )

    payload = {
        "jsonrpc": "2.0",
        "id": "holders",
        "method": "getTokenLargestAccounts",
        "params": [
            token_address
        ]
    }

    response = httpx.post(
        url,
        json=payload,
        timeout=20
    )

    if response.status_code != 200:
        return []

    result = response.json()

    return result.get("result", {}).get("value", [])