from packages.config.settings import (
    EXCLUDED_TICKERS,
    TRUSTED_DEXES,
    MIN_LIQUIDITY,
    MIN_VOLUME,
    MIN_MARKET_CAP,
    SUPPORTED_CHAINS,
)


def is_supported_chain(pair):
    return pair.get("chain") in SUPPORTED_CHAINS


def is_not_major_token(pair):
    return pair.get("ticker", "").upper() not in EXCLUDED_TICKERS


def has_minimum_liquidity(pair):
    return pair.get("liquidity", 0) >= MIN_LIQUIDITY


def has_minimum_volume(pair):
    return pair.get("volume", 0) >= MIN_VOLUME


def has_reasonable_market_cap(pair):
    return pair.get("market_cap", 0) >= MIN_MARKET_CAP


def is_trusted_dex(pair):

    # Birdeye tokens don't expose DEX information
    if pair.get("source") == "Birdeye":
        return True

    return pair.get("dex") in TRUSTED_DEXES


def is_candidate(pair):

    return (
        is_supported_chain(pair)
        and is_not_major_token(pair)
        and has_minimum_liquidity(pair)
        and has_minimum_volume(pair)
        and has_reasonable_market_cap(pair)
        and is_trusted_dex(pair)
    )
# Backward compatibility
def is_solana(pair):
    return is_supported_chain(pair)