from dataclasses import dataclass


@dataclass
class Token:

    symbol: str

    name: str

    liquidity_usd: float

    market_cap: float

    holders: int

    volume_24h: float

    buys: int

    sells: int

    chain: str = "solana"