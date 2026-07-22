def detect_whales(profile):

    whales = 0

    if profile["buy_volume"] > 500000:
        whales += 1

    if profile["holders"] > 1000:
        whales += 1

    if profile["wallet_growth"] > 5:
        whales += 1

    return whales