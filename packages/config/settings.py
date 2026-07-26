"""
ASILI Intelligence Engine
Global Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")
BIRDEYE_API_KEY = os.getenv("BIRDEYE_API_KEY")


# ==========================
# Market Filters
# ==========================

MIN_LIQUIDITY = 25_000

MIN_VOLUME = 10_000

MIN_MARKET_CAP = 100_000


# ==========================
# Alpha Scoring
# ==========================

LOW_LIQUIDITY = 25_000
LOW_VOLUME = 10_000

SMALL_MARKET_CAP = 100_000
MEDIUM_MARKET_CAP = 5_000_000
LARGE_MARKET_CAP = 20_000_000

HIGH_LIQUIDITY = 500_000

MEDIUM_LIQUIDITY = 100_000

HIGH_VOLUME = 500_000

MEDIUM_VOLUME = 100_000


# ==========================
# Radar
# ==========================

MIN_ALPHA_FOR_RADAR = 70

MAX_REPORT_SIZE = 20


# ==========================
# Supported Chains
# ==========================

SUPPORTED_CHAINS = [
    "solana"
]


# ==========================
# Trusted DEXs
# ==========================

TRUSTED_DEXES = [
    "raydium",
    "orca",
    "meteora",
    "pumpfun"
]


# ==========================
# Major Tokens
# ==========================

EXCLUDED_TICKERS = [
    "SOL",
    "USDC",
    "USDT",
    "BTC",
    "ETH",
    "BNB",
    "WBTC",
    "WETH"
]