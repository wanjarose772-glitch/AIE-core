import httpx

from packages.config import HELIUS_API_KEY


URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"


def get_token_metadata(mint):

    payload = {
        "jsonrpc": "2.0",
        "id": "hawk",
        "method": "getAsset",
        "params": {
            "id": mint
        }
    }

    response = httpx.post(
        URL,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        return {}

    data = response.json()

    result = data.get("result", {})

    content = result.get("content", {})

    metadata = content.get("metadata", {})

    links = content.get("links", {})

    return {

        "name": metadata.get("name"),

        "symbol": metadata.get("symbol"),

        "description": metadata.get("description"),

        "image": links.get("image"),

        "website": links.get("external_url"),

        "attributes": metadata.get("attributes"),

    }