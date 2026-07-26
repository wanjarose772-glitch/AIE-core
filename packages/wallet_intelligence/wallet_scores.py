"""
Wallet Reputation Engine
"""


def calculate_wallet_score(wallet):

    score = 0

    score += wallet.winning_trades * 15

    score -= wallet.losing_trades * 8

    score -= wallet.rugs_bought * 20

    score += wallet.highest_roi / 10

    wallet.confidence = score

    if score > 300:
        wallet.grade = "A+"

    elif score > 200:
        wallet.grade = "A"

    elif score > 120:
        wallet.grade = "B"

    elif score > 50:
        wallet.grade = "C"

    else:
        wallet.grade = "NEW"

    return wallet