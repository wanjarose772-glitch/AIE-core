SMART_WALLETS = {

    "PEPE": 18,
    "BONK": 11,
    "DOG": 6,
    "W26": 2,
    "HOOD": 1,
    "MET": 5

}


def get_smart_wallet_count(token):

    return SMART_WALLETS.get(
        token["ticker"],
        0
    )
def calculate_smart_money_score(token):

    wallets = get_smart_wallet_count(token)

    if wallets >= 15:
        return 30

    if wallets >= 10:
        return 20

    if wallets >= 5:
        return 10

    return 0
def smart_money_rating(score):

    if score >= 30:
        return "🐋 Heavy Accumulation"

    if score >= 20:
        return "🐬 Accumulating"

    if score >= 10:
        return "👀 Early Interest"

    return "None"