def analyze_metadata(token):

    score = 0

    metadata = {
        "website": False,
        "twitter": False,
        "telegram": False,
        "discord": False,
    }

    extensions = token.get("extensions", {})

    # -----------------------
    # Website
    # -----------------------

    if extensions.get("website"):
        metadata["website"] = True
        score += 20

    # -----------------------
    # Twitter / X
    # -----------------------

    if extensions.get("twitter"):
        metadata["twitter"] = True
        score += 20

    # -----------------------
    # Telegram
    # -----------------------

    if extensions.get("telegram"):
        metadata["telegram"] = True
        score += 20

    # -----------------------
    # Discord
    # -----------------------

    if extensions.get("discord"):
        metadata["discord"] = True
        score += 20

    metadata["community_score"] = score

    return metadata