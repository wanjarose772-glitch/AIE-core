import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HELIUS_API_KEY")

print("API FOUND:", API_KEY is not None)

url = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getSlot"
}

response = httpx.post(url, json=payload)

print("Status:", response.status_code)
print(response.text)