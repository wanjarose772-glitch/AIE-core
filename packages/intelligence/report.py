from packages.source_manager.manager import collect_market_data

from packages.normalizers.market import normalize_pair
from packages.normalizers.birdeye import normalize_birdeye_token

from packages.filters.quality import is_candidate

from packages.intelligence.analyzer import analyze_token

from packages.history.storage import save_snapshot


def build_intelligence_report():
    """
    Build the complete intelligence report.
    """

    market = collect_market_data()

    report = []

    for item in market:

        # Normalize according to source
        if "baseToken" in item:
            token = normalize_pair(item)
        else:
            token = normalize_birdeye_token(item)

        # Skip low-quality tokens
        if not is_candidate(token):
            continue

        # Run the intelligence pipeline
        token = analyze_token(token, item)

        report.append(token)

    # Sort by Alpha Score
    report.sort(
        key=lambda x: x["alpha_score"],
        reverse=True
    )

    # Keep only the best opportunities
    report = report[:20]

    # Save snapshot
    save_snapshot(report)

    return report