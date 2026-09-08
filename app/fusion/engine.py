"""
AIE Fusion Engine v2
"""

from app.fusion.models import (
    EngineResult,
    FusionInput,
)


class FusionEngine:

    def fuse(self, data: FusionInput) -> EngineResult:

        score = round(

            (
                data.narrative * 0.30
                + data.liquidity * 0.15
                + data.momentum * 0.20
                + data.whales * 0.15
                + data.community * 0.10
                + data.risk * 0.10
            )

        )

        recommendation = "WATCH"

        if score >= 90:
            recommendation = "BUY"

        elif score >= 75:
            recommendation = "ACCUMULATE"

        warnings = []

        if data.risk < 60:
            warnings.append("High rug risk")

        if data.community < 50:
            warnings.append("Weak organic community")

        reasoning = [

            f"Narrative {data.narrative}",

            f"Liquidity {data.liquidity}",

            f"Momentum {data.momentum}",

            f"Whales {data.whales}",

            f"Community {data.community}",

            f"Risk {data.risk}",

        ]

        return EngineResult(

            engine="Fusion Engine",

            score=score,

            confidence=95,

            recommendation=recommendation,

            reasoning=reasoning,

            warnings=warnings,

        )