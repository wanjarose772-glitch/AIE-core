"""
AIE Wallet Engine
"""

from packages.wallet_engine.collector import collect_wallets
from packages.wallet_engine.scorer import score_wallets
from packages.wallet_engine.labels import wallet_rating


class WalletEngine:

    def analyze(self, token):

        # --------------------------
        # Get token address
        # --------------------------

        address = token.get("address", "")

        if not isinstance(address, str):
            address = ""

        # Remove GeckoTerminal prefix if present
        address = address.removeprefix("solana_").strip()

        print("\n============================")
        print("WALLET ENGINE")
        print("============================")
        print("Wallet lookup:", address)

        # --------------------------
        # No address
        # --------------------------

        if not address:

            token["wallets"] = []
            token["wallet_score"] = 0
            token["wallet_rating"] = "POOR"

            return token

        # --------------------------
        # Collect holders
        # --------------------------

        try:

            wallets = collect_wallets(address)

        except Exception as e:

            print("Wallet Engine Error")
            print(e)

            wallets = []

        # --------------------------
        # Score wallets
        # --------------------------

        score = score_wallets(wallets)

        token["wallets"] = wallets
        token["wallet_score"] = score
        token["wallet_rating"] = wallet_rating(score)

        return token