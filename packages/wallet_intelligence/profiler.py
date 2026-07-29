"""
Wallet Profiler

Profiles wallets against the
local smart wallet database.
"""

from packages.wallet_intelligence.wallet_database import (
    get_wallet,
)


def profile_wallets(wallets):

    profiled = []

    for item in wallets:

        wallet = get_wallet(item["address"])

        wallet.address = item["address"]
        wallet.amount = item["amount"]

        profiled.append(wallet)

    return profiled