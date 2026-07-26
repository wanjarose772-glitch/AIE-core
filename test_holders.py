import httpx

from packages.config import HELIUS_API_KEY

url = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTokenLargestAccounts",
    "params": [
        "So11111111111111111111111111111111111111112"
    ]
}

response = httpx.post(
    url,
    json=payload,
    timeout=20
)

print(response.json())