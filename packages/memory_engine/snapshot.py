"""
Snapshot Model

Represents one market snapshot for a token.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Snapshot:

    address: str

    symbol: str

    timestamp: datetime

    price: float

    market_cap: float

    liquidity: float

    volume: float

    holders: int

    buys: int

    sells: int