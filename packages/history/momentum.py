def calculate_momentum(change):

    score = 0

    # Liquidity
    if change["liquidity_change"] >= 100:
        score += 40
    elif change["liquidity_change"] >= 50:
        score += 30
    elif change["liquidity_change"] >= 20:
        score += 20
    elif change["liquidity_change"] > 0:
        score += 10

    # Volume
    if change["volume_change"] >= 100:
        score += 40
    elif change["volume_change"] >= 50:
        score += 30
    elif change["volume_change"] >= 20:
        score += 20
    elif change["volume_change"] > 0:
        score += 10

    # Confidence
    if change["confidence_change"] > 10:
        score += 10
    elif change["confidence_change"] > 0:
        score += 5

    # Alpha
    if change["alpha_change"] > 10:
        score += 10
    elif change["alpha_change"] > 0:
        score += 5

    return score


def momentum_rating(score):

    if score >= 80:
        return "🚀 Exploding"

    elif score >= 60:
        return "🔥 Very Strong"

    elif score >= 40:
        return "📈 Rising Fast"

    elif score >= 20:
        return "👀 Building"

    elif score > 0:
        return "🙂 Early"

    return "😴 Flat"