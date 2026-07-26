"""
Smart Wallet Detector
"""

from packages.wallet_intelligence.wallet_database import get_wallet


def detect_smart_wallets(wallet_addresses):

    smart_wallets = []

    confidence_bonus = 0

    for address in wallet_addresses:

        wallet = get_wallet(address)

        if wallet.grade == "A+":

            smart_wallets.append(wallet)
            confidence_bonus += 20

        elif wallet.grade == "A":

            smart_wallets.append(wallet)
            confidence_bonus += 15

        elif wallet.grade == "B":

            smart_wallets.append(wallet)
            confidence_bonus += 10

    return {
        "count": len(smart_wallets),
        "wallets": smart_wallets,
        "confidence_bonus": confidence_bonus
    }