import json
import os

from packages.history.momentum import (
    calculate_momentum,
    momentum_rating
)

from packages.history.new_listing import (
    detect_new_listing,
    listing_status
)

from packages.signals.liquidity import liquidity_signal

SNAPSHOT_FOLDER = "snapshots"


def load_latest_snapshots():

    files = sorted(os.listdir(SNAPSHOT_FOLDER))

    if len(files) < 2:
        return None, None

    previous = os.path.join(SNAPSHOT_FOLDER, files[-2])
    latest = os.path.join(SNAPSHOT_FOLDER, files[-1])

    with open(previous, "r", encoding="utf-8") as file:
        old_report = json.load(file)

    with open(latest, "r", encoding="utf-8") as file:
        new_report = json.load(file)

    return old_report, new_report


def percentage_change(old, new):

    if old == 0:
        return 0

    return round(((new - old) / old) * 100, 2)


def compare_snapshots():

    old_report, new_report = load_latest_snapshots()

    if old_report is None:
        return []

    old_tokens = {
        token["ticker"]: token
        for token in old_report
    }

    comparison = []

    for token in new_report:

        ticker = token["ticker"]

        is_new = detect_new_listing(
            ticker,
            old_tokens
        )

        if is_new:

            comparison.append({

                "ticker": ticker,
                "status": listing_status(True),
                "momentum": "🚀 Brand New"

            })

            continue

        previous = old_tokens[ticker]

        liquidity_change = percentage_change(
            previous["liquidity"],
            token["liquidity"]
        )

        volume_change = percentage_change(
            previous["volume"],
            token["volume"]
        )

        change = {

            "ticker": ticker,

            "liquidity_change": liquidity_change,

            "volume_change": volume_change,

            "confidence_change":
                token["confidence"] - previous["confidence"],

            "alpha_change":
                token["alpha_score"] - previous["alpha_score"]

        }

        change["momentum_score"] = calculate_momentum(change)

        change["momentum"] = momentum_rating(
            change["momentum_score"]
        )

        change["liquidity_signal"] = liquidity_signal(
            liquidity_change
        )

        comparison.append(change)

    comparison.sort(
        key=lambda x: x.get("momentum_score", 100),
        reverse=True
    )

    return comparison