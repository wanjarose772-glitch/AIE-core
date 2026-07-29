"""
Smart Wallet Intelligence
"""


def analyze_wallets(wallets):

    score = 0

    smart_wallets = 0

    for wallet in wallets:

        grade = getattr(wallet, "grade", "C")

        if grade == "A+":

            smart_wallets += 1
            score += 20

        elif grade == "A":

            smart_wallets += 1
            score += 15

        elif grade == "B":

            smart_wallets += 1
            score += 10

    return {
        "wallet_score": min(score, 100),
        "smart_wallets": smart_wallets,
        "wallets": wallets,
    }