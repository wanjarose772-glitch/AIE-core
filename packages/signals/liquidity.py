def liquidity_signal(change):

    if change >= 300:
        return "💥 Massive Liquidity"

    elif change >= 150:
        return "🔥 Liquidity Explosion"

    elif change >= 75:
        return "🚀 Strong Liquidity"

    elif change >= 25:
        return "📈 Liquidity Rising"

    elif change > 0:
        return "🙂 Slight Increase"

    elif change <= -50:
        return "⚠️ Liquidity Leaving"

    return "➖ Stable"