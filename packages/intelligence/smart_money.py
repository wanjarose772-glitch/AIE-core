"""
Legacy Smart Money compatibility layer.

The old Smart Money engine depended on Birdeye metrics like:

- unique_wallet_1h
- buy_1h
- sell_1h

The new engine uses Wallet Intelligence instead.
"""


def calculate_smart_money(data):
    """
    Compatibility function.

    If wallet intelligence already calculated a score,
    return it.

    Otherwise return 0.
    """
    return data.get("wallet_score", 0)


def smart_money_label(score):

    if score >= 80:
        return "🐋 Heavy Accumulation"

    if score >= 60:
        return "🟢 Strong Buying"

    if score >= 40:
        return "🟡 Moderate Interest"

    if score >= 20:
        return "⚪ Weak"

    return "🔴 None"