"""
AIE Token Identity Resolver
"""

from packages.token_identity.birdeye import resolve_birdeye


def resolve_identity(token: dict):

    # Already identified
    if token.get("ticker") != "UNKNOWN":
        return token

    address = token.get("address")

    if not address:
        return token

    metadata = resolve_birdeye(address)

    if metadata:

        token["ticker"] = metadata.get(
            "symbol",
            token["ticker"],
        )

        token["symbol"] = metadata.get(
            "symbol",
            token["symbol"],
        )

        token["name"] = metadata.get(
            "name",
            token["name"],
        )

        token["logo"] = metadata.get("logoURI")

        token["decimals"] = metadata.get("decimals")

    return token