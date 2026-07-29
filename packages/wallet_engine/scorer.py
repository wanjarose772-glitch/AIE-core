def score_wallets(wallets):

    if not wallets:
        return 0

    score = 50

    if len(wallets) > 25:
        score += 15

    if len(wallets) > 50:
        score += 15

    biggest = max(
        wallet["percentage"]
        for wallet in wallets
    )

    if biggest < 10:
        score += 20

    elif biggest > 30:
        score -= 30

    return max(0, min(score, 100))