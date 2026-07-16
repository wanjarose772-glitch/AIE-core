from packages.intelligence.metadata import analyze_metadata

from packages.intelligence.narrative import (
    calculate_narrative_score,
    get_narrative,
)

from packages.intelligence.smart_money import (
    get_smart_wallet_count,
    calculate_smart_money_score,
    smart_money_rating,
)

from packages.intelligence.social_signals import (
    get_social_score,
    social_rating,
)

from packages.intelligence.confidence import (
    calculate_confidence,
)

from packages.intelligence.recommendation import (
    get_recommendation,
)

from packages.score_engine.engine import (
    calculate_alpha_score,
)


def analyze_token(token, raw_item):

    # Metadata
    metadata = analyze_metadata(raw_item)
    token.update(metadata)

    # Alpha
    token["alpha_score"] = calculate_alpha_score(token)

    # Narrative
    token["narrative_score"] = calculate_narrative_score(token)
    token["narrative"] = get_narrative(token)

    # Smart Money
    token["smart_wallets"] = get_smart_wallet_count(token)

    token["smart_money_score"] = (
        calculate_smart_money_score(token)
    )

    token["smart_money"] = smart_money_rating(
        token["smart_money_score"]
    )

    # Social
    token["social_score"] = get_social_score(token)

    token["social"] = social_rating(
        token["social_score"]
    )

    # Confidence
    token["confidence"] = calculate_confidence(token)

    # Recommendation
    token["recommendation"] = get_recommendation(
        token["alpha_score"],
        token["confidence"]
    )

    return token