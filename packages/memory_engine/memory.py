"""
Memory Engine

Stores and retrieves token history.
"""

from datetime import datetime

from packages.memory_engine.snapshot import Snapshot
from packages.memory_engine.storage import memory_db


class MemoryEngine:

    def save(self, token):

        address = token["address"]

        snapshot = Snapshot(
            address=address,
            symbol=token.get("symbol", ""),
            timestamp=datetime.now(),
            price=token.get("price", 0),
            market_cap=token.get("market_cap", 0),
            liquidity=token.get("liquidity_usd", 0),
            volume=token.get("volume_24h", 0),
            holders=token.get("holders", 0),
            buys=token.get("buys", 0),
            sells=token.get("sells", 0),
        )

        if address not in memory_db:
            memory_db[address] = []

        memory_db[address].append(snapshot)

        return snapshot

    def history(self, address):

        return memory_db.get(address, [])

    def latest(self, address):

        history = self.history(address)

        if history:
            return history[-1]

        return None

    def previous(self, address):

        history = self.history(address)

        if len(history) >= 2:
            return history[-2]

        return None