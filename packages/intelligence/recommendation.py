def get_recommendation(alpha_score, confidence):
    """
    Generate an investment recommendation based on
    alpha score and confidence.
    """

    if alpha_score >= 90 and confidence >= 100:
        return "🔥 BUY"

    if alpha_score >= 80:
        return "⭐ STRONG WATCH"

    if alpha_score >= 70:
        return "👀 WATCH"

    return "⚠ AVOID"