"""
Smart Wallet Tracker
"""

from packages.wallet_intelligence.profiler import profile_wallet


class WalletTracker:
    """
    Tracks wallets interacting with a token and profiles them.
    """

    def __init__(self):
        self.detected_wallets = []

    def process_token(self, token: dict):

        wallet_addresses = token.get("wallets", [])

        profiled_wallets = []

        for address in wallet_addresses:

            wallet = profile_wallet(address)

            profiled_wallets.append(wallet)

        return profiled_wallets