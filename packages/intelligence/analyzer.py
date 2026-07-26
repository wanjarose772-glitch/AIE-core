from packages.database import token
from packages.wallet_intelligence.smart_wallets import (
    analyze_wallets,
)

from packages.intelligence.smart_money import (
    calculate_smart_money,
    smart_money_label,
)

from packages.intelligence.metadata import (
    analyze_metadata,
)

from packages.intelligence.narrative import (
    calculate_narrative_score,
    get_narrative,
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


def analyze_token(
    token,
    metadata_item,
    trade_data,
    wallet_data,
):

    # ----------------------------
    # Metadata
    # ----------------------------

    metadata = analyze_metadata(metadata_item)
    token.update(metadata)

    # ----------------------------
    # Wallet Intelligence
    # ----------------------------

    wallets = analyze_wallets(wallet_data)
    token.update(wallets)

    # ----------------------------
    # Smart Money
    # ----------------------------

    token["smart_money_score"] = calculate_smart_money(
        trade_data
    )

    token["smart_money"] = smart_money_label(
        token["smart_money_score"]
    )

    # ----------------------------
    # Alpha Score
    # ----------------------------

    token["alpha_score"] = calculate_alpha_score(
        token
    )

    from packages.intelligence.confidence import calculate_confidence

    token["confidence"] = calculate_confidence(token)
    # ----------------------------
    # Narrative
    # ----------------------------

    token["narrative_score"] = calculate_narrative_score(
        token
    )

    token["narrative"] = get_narrative(
        token
    )

    # ----------------------------
    # Social
    # ----------------------------

    token["social_score"] = get_social_score(
        token
    )

    token["social"] = social_rating(
        token["social_score"]
    )

    # ----------------------------
    # Confidence
    # ----------------------------

    token["confidence"] = calculate_confidence(
        token
    )

    # ----------------------------
    # Recommendation
    # ----------------------------

    token["recommendation"] = get_recommendation(
        token["alpha_score"],
        token["confidence"],
    )

    return token