from packages.filters.quality import (
    is_solana,
    is_not_major_token,
    has_minimum_liquidity,
    has_minimum_volume,
    has_reasonable_market_cap,
    is_trusted_dex,
)


def inspect_token(token):
    """
    Explain why a token passed or failed the Discovery Gate.
    """

    report = {
        "ticker": token.get("ticker"),
        "chain": is_solana(token),
        "major_token": is_not_major_token(token),
        "liquidity": has_minimum_liquidity(token),
        "volume": has_minimum_volume(token),
        "market_cap": has_reasonable_market_cap(token),
        "trusted_dex": is_trusted_dex(token),
    }

    report["candidate"] = all([
        report["chain"],
        report["major_token"],
        report["liquidity"],
        report["volume"],
        report["market_cap"],
        report["trusted_dex"],
    ])

    return report