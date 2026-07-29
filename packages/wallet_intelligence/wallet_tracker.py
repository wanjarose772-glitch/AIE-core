"""
Smart Wallet Tracker
"""

from packages.wallet_intelligence.profiler import profile_wallets


class WalletTracker:
    """
    Tracks wallets interacting with a token.
    """

    def process_token(self, token: dict):

        wallets = token.get("wallets", [])

        return 