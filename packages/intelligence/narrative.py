MEME_KEYWORDS = {
    "dog",
    "cat",
    "pepe",
    "frog",
    "ape",
    "meme",
    "moon",
    "pump",
    "bonk",
    "wojak",
    "chad",
    "degen",
    "elon",
    "trump",
    "ai",
    "agent",
    "robot",
    "grok",
    "banana",
    "penguin",
    "shark",
    "sol",
    "coin"
}


BLACKLIST_KEYWORDS = {
    "wrapped",
    "usd",
    "usdc",
    "usdt",
    "stock",
    "security",
    "bond",
    "fund",
    "etf",
    "backpack",
    "lending",
    "yield"
}
def calculate_narrative_score(token):

    text = (
        token.get("ticker", "") +
        " " +
        token.get("name", "")
    ).lower()

    score = 0

    for word in MEME_KEYWORDS:
        if word in text:
            score += 15

    for word in BLACKLIST_KEYWORDS:
        if word in text:
            score -= 25

    return max(score, 0)
def get_narrative(token):

    score = calculate_narrative_score(token)

    if score >= 40:
        return "🔥 Strong Meme"

    if score >= 20:
        return "⭐ Emerging Narrative"

    return "Generic"