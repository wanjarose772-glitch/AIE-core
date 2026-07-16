from packages.source_manager.manager import collect_market_data
from packages.normalizers.market import normalize_pair
from packages.filters.quality import is_candidate
from packages.score_engine.engine import calculate_alpha_score


def run_pipeline():
    """
    Run the AIE market intelligence pipeline.
    """

    market_data = collect_market_data()

    candidates = []

    for pair in market_data:

        normalized = normalize_pair(pair)

        if is_candidate(normalized):

            normalized["alpha_score"] = calculate_alpha_score(normalized)

            candidates.append(normalized)

    candidates.sort(
        key=lambda token: token["alpha_score"],
        reverse=True
    )

    return candidates