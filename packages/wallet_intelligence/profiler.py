"""
Wallet Profiler
"""

from packages.wallet_intelligence.wallet_database import (
    get_wallet,
    save_wallet,
)

from packages.wallet_intelligence.wallet_scores import (
    calculate_wallet_score,
)


def profile_wallet(address: str):

    wallet = get_wallet(address)

    wallet.times_seen += 1

    calculate_wallet_score(wallet)

    save_wallet(wallet)

    return wallet