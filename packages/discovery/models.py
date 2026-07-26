from dataclasses import dataclass
from typing import Optional


@dataclass
class DiscoveryToken:
    source: str

    ticker: str

    name: str

    address: str

    price: float

    liquidity: float

    volume: float

    created_at: Optional[str]

    dex: str

    age_minutes: float = 0

    discovery_score: int = 0

    rating: str = "UNKNOWN"