import httpx
import json

url = "https://api.geckoterminal.com/api/v2/networks/solana/new_pools"

response = httpx.get(url)

data = response.json()

print("TOP LEVEL")
print(data.keys())

print()

print("INCLUDED LENGTH")
print(len(data.get("included", [])))

print()

print("FIRST INCLUDED OBJECT")

print(
    json.dumps(
        data.get("included", [])[0],
        indent=2
    )
)