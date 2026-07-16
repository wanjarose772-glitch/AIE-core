def analyze_metadata(token):

    score = 0

    info = token.get("info", {})

    websites = info.get("websites", [])
    socials = info.get("socials", [])

    metadata = {
        "website": False,
        "twitter": False,
        "telegram": False,
        "discord": False
    }

    if websites:
        metadata["website"] = True
        score += 20

    for social in socials:

        social_type = social.get("type", "").lower()

        if social_type == "twitter":
            metadata["twitter"] = True
            score += 20

        elif social_type == "telegram":
            metadata["telegram"] = True
            score += 20

        elif social_type == "discord":
            metadata["discord"] = True
            score += 20

    metadata["community_score"] = score

    return metadata