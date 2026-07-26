"""
Wallet Intelligence Model
"""

from dataclasses import dataclass


@dataclass
class Wallet:

    address: str

    times_seen: int = 0

    winning_trades: int = 0

    losing_trades: int = 0

    average_roi: float = 0.0

    highest_roi: float = 0.0

    rugs_bought: int = 0

    confidence: float = 0.0

    grade: str = "NEW"