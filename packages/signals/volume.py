def volume_signal(change):

    if change >= 300:
        return "💥 Massive Volume"

    elif change >= 150:
        return "🚀 Volume Explosion"

    elif change >= 75:
        return "🔥 Heavy Trading"

    elif change >= 25:
        return "📈 Volume Rising"

    elif change > 0:
        return "🙂 Slight Increase"

    elif change <= -50:
        return "⚠️ Volume Falling"

    return "➖ Stable"