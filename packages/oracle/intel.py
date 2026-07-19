from packages.oracle.providers.birdeye import get_token_overview


def enrich(token):

    address = token["address"]

    try:

        info = get_token_overview(address)

    except Exception:

        return token

    token["price"] = info.get("price", token.get("price"))

    token["market_cap"] = info.get("marketCap", token.get("market_cap"))

    token["liquidity"] = info.get("liquidity", token.get("liquidity"))

    token["volume"] = info.get("v24hUSD", token.get("volume"))

    token["holders"] = info.get("holder", 0)

    token["logo"] = info.get("logoURI", token.get("logo"))

    token["website"] = info.get("website", "")

    token["twitter"] = info.get("twitter", "")

    token["telegram"] = info.get("telegram", "")

    return token