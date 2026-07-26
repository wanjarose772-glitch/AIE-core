from datetime import datetime
from datetime import timezone


def score_launch(token):

    score = 0

    liquidity = token.get("liquidity", 0)

    volume = token.get("volume", 0)

    dex = (token.get("dex") or "").lower()

    created_at = token.get("created_at")

    # -------------------------
    # Liquidity
    # -------------------------

    if 2000 <= liquidity <= 10000:
        score += 20

    elif 10000 <= liquidity <= 50000:
        score += 30

    elif liquidity > 50000:
        score += 20

    # -------------------------
    # Volume
    # -------------------------

    if volume > 500:
        score += 15

    if volume > 5000:
        score += 15

    if volume > 50000:
        score += 20

    # -------------------------
    # DEX
    # -------------------------

    if dex == "pump-fun":
        score += 10

    elif dex == "pumpswap":
        score += 15

    elif dex.startswith("meteora"):
        score += 20

    # -------------------------
    # Age Bonus
    # -------------------------

    age_minutes = None

    if created_at:

        try:

            launch_time = datetime.fromisoformat(
                created_at.replace("Z", "+00:00")
            )

            now = datetime.now(timezone.utc)

            age_minutes = (
                now - launch_time
            ).total_seconds() / 60

            token["age_minutes"] = round(
                age_minutes,
                2
            )

            if age_minutes < 5:
                score += 25

            elif age_minutes < 15:
                score += 20

            elif age_minutes < 30:
                score += 15

            elif age_minutes < 60:
                score += 10

        except Exception:

            token["age_minutes"] = None

        # Keep discovery score between 0 and 100
    score = min(score, 100)

    token["discovery_score"] = score

    if score >= 80:
        token["rating"] = "🔥 HIGH"

    elif score >= 60:
        token["rating"] = "🟢 GOOD"

    elif score >= 40:
        token["rating"] = "🟡 WATCH"

    else:
        token["rating"] = "⚪ LOW"

    return token