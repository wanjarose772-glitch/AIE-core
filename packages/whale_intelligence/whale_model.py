"""
Whale Intelligence Model
"""

from dataclasses import dataclass


@dataclass
class Whale:

    address: str

    total_bought: float = 0.0
    total_sold: float = 0.0

    buy_count: int = 0
    sell_count: int = 0

    net_position: float = 0.0

    first_seen: str = ""
    last_seen: str = ""

    confidence: float = 0.0

    grade: str = "UNKNOWN"