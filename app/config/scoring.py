"""
Global scoring thresholds.
Every engine imports these values.
"""

# ----------------------------
# LIQUIDITY
# ----------------------------

MIN_LIQUIDITY = 10_000
GOOD_LIQUIDITY = 50_000
EXCELLENT_LIQUIDITY = 250_000

# ----------------------------
# MARKET CAP
# ----------------------------

MICRO_CAP = 100_000
SMALL_CAP = 1_000_000
MID_CAP = 10_000_000

# ----------------------------
# HOLDERS
# ----------------------------

MIN_HOLDERS = 100
GOOD_HOLDERS = 500
EXCELLENT_HOLDERS = 2000

# ----------------------------
# VOLUME
# ----------------------------

MIN_VOLUME = 5_000
GOOD_VOLUME = 50_000
EXCELLENT_VOLUME = 500_000

# ----------------------------
# BUY / SELL
# ----------------------------

GOOD_BUY_RATIO = 1.20

# ----------------------------
# SCORE LIMITS
# ----------------------------

MAX_SCORE = 100
MIN_SCORE = 0