"""
Confidence Rating
"""


def confidence_rating(score):

    if score >= 90:
        return "🔥 STRONG BUY"

    elif score >= 75:
        return "🟢 BUY"

    elif score >= 60:
        return "🟡 WATCH"

    elif score >= 40:
        return "⚪ LOW"

    return "🔴 AVOID"