def get_priority(token):

    confidence = token["confidence"]
    alpha = token["alpha_score"]

    if confidence >= 80 and alpha >= 90:
        return "🔥 CRITICAL"

    if confidence >= 60:
        return "⭐ HIGH"

    if confidence >= 40:
        return "👀 WATCH"

    return "💤 LOW"