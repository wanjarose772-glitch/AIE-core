from packages.metadata_engine.birdeye import get_birdeye_metadata
from packages.metadata_engine.helius import get_helius_metadata
from packages.metadata_engine.jupiter import get_jupiter_metadata


def enrich_metadata(token):

    address = token.get("address")

    if not address:
        return token

    # ---------------------------------
    # Safely fetch metadata
    # ---------------------------------

    try:
        birdeye = get_birdeye_metadata(address) or {}
    except Exception:
        birdeye = {}

    try:
        helius = get_helius_metadata(address) or {}
    except Exception:
        helius = {}

    try:
        jupiter = get_jupiter_metadata(address) or {}
    except Exception:
        jupiter = {}

    # ---------------------------------
    # Identity
    # Never overwrite existing values
    # unless a provider has something better.
    # ---------------------------------

    token["ticker"] = (
        birdeye.get("symbol")
        or helius.get("symbol")
        or jupiter.get("symbol")
        or token.get("ticker")
        or "UNKNOWN"
    )

    token["symbol"] = token["ticker"]

    token["name"] = (
        birdeye.get("name")
        or helius.get("name")
        or jupiter.get("name")
        or token.get("name")
        or token["ticker"]
    )

    # ---------------------------------
    # Optional metadata
    # ---------------------------------

    token["logo"] = (
        birdeye.get("logoURI")
        or helius.get("image")
        or jupiter.get("logoURI")
        or token.get("logo")
    )

    token["market_cap"] = (
        birdeye.get("mc")
        or token.get("market_cap", 0)
    )

    token["fdv"] = (
        birdeye.get("fdv")
        or token.get("fdv", 0)
    )

    token["decimals"] = (
        birdeye.get("decimals")
        or helius.get("decimals")
        or token.get("decimals")
    )

    token["verified"] = (
        birdeye.get("verified")
        or token.get("verified", False)
    )

    return token