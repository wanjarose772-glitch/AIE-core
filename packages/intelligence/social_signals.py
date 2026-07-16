SOCIAL_SCORE = {

    "PEPE": 95,
    "BONK": 85,
    "DOG": 60,
    "W26": 40,
    "HOOD": 15,
    "MET": 75

}


def get_social_score(token):

    return SOCIAL_SCORE.get(
        token["ticker"],
        5
    )


def social_rating(score):

    if score >= 90:
        return "🔥 Viral"

    if score >= 70:
        return "📈 Trending"

    if score >= 40:
        return "👀 Growing"

    return "Quiet"