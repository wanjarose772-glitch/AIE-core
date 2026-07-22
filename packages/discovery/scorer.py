def score_new_pair(pair):

    score = 0

    liquidity = pair["liquidity"]
    volume = pair["volume"]

    if liquidity > 10000:
        score += 20

    if liquidity > 25000:
        score += 20

    if volume > liquidity:
        score += 20

    if volume > liquidity * 2:
        score += 20

    if pair["pair_created"]:
        score += 20

    return min(score, 100)