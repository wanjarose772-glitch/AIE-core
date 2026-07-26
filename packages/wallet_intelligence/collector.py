"""
Wallet Collector
"""

import httpx

from packages.config.settings import HELIUS_API_KEY

HELIUS_URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"


def get_token_wallets(token_address: str, limit: int = 25):

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenLargestAccounts",
        "params": [
            token_address
        ]
    }

    response = httpx.post(
        HELIUS_URL,
        json=payload,
        timeout=20
    )

    data = response.json()

    wallets = []

    if "result" in data:

        for account in data["result"]["value"][:limit]:

            wallets.append({
                "address": account["address"],
                "amount": account.get("uiAmount", 0) or 0
            })

    return wallets


# --------------------------------------------------------
# Compatibility wrapper
# --------------------------------------------------------

def collect_wallet_data(token_address):
    """
    Temporary wrapper so existing code keeps working.
    """

    from packages.wallet_intelligence.profiler import profile_wallets


def collect_wallet_data(token_address):

    wallets = get_token_wallets(token_address)

    return profile_wallets(wallets)