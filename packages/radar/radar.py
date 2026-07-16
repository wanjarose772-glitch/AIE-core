from packages.intelligence.report import build_intelligence_report

from packages.config.settings import MIN_ALPHA_FOR_RADAR

from packages.radar.reasons import get_reasons

from packages.radar.priority import get_priority


def build_alpha_radar():

    report = build_intelligence_report()

    radar = []

    for token in report:

        if token["alpha_score"] < MIN_ALPHA_FOR_RADAR:
            continue

        radar.append({

            "ticker": token["ticker"],

            "name": token["name"],

            "alpha_score": token["alpha_score"],

            "confidence": token["confidence"],

            "priority": get_priority(token),

            "reasons": get_reasons(token),

            "recommendation": token["recommendation"]

        })

    radar.sort(

        key=lambda x: (
            x["confidence"],
            x["alpha_score"]
        ),

        reverse=True

    )

    return radar