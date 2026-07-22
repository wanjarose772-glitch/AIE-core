from packages.wallet_intelligence.profiler import build_wallet_profile


def analyze_wallets(wallet_data):

    if not wallet_data:

        return {
            "wallet_score": 0,
            "whales": 0,
            "wallet_rating": "Unknown"
        }

    profile = build_wallet_profile(wallet_data)

    score = 0

    # Holder count
    if profile["holders"] > 1000:
        score += 20

    # Number of large wallets
    if profile["largest_wallets"] >= 10:
        score += 30

    # Whale wallets
    if profile["whale_wallets"] >= 3:
        score += 30

    # Whale supply
    if profile["whale_supply"] > 0:
        score += 20

    if score >= 80:
        rating = "Institutional"

    elif score >= 60:
        rating = "Accumulation"

    elif score >= 40:
        rating = "Watching"

    else:
        rating = "Weak"

    return {

        "wallet_score": score,

        "whales": profile["whale_wallets"],

        "wallet_rating": rating
    }