"""
Whale Tracker
"""

from packages.whale_intelligence.whale_database import (
    get_whale,
    save_whale,
)

from packages.whale_intelligence.whale_engine import WhaleEngine


class WhaleTracker:

    def __init__(self):

        self.engine = WhaleEngine()

    def process_token(self, token):

        whales = []

        transactions = token.get("whales", [])

        for tx in transactions:

            whale = get_whale(tx["address"])

            whale.buy_count += tx.get("buys", 0)

            whale.sell_count += tx.get("sells", 0)

            whale.total_bought += tx.get("buy_volume", 0)

            whale.total_sold += tx.get("sell_volume", 0)

            whale.net_position = (
                whale.total_bought -
                whale.total_sold
            )

            whale = self.engine.analyze(whale)

            save_whale(whale)

            whales.append(whale)

        return whales