"""
AIE Narrative Confidence Engine

This module calculates how strong a narrative is based on
multiple weighted factors.

Later these values will come from:
- News APIs
- X (Twitter)
- Reddit
- Google Trends
- Community analysis
"""

from dataclasses import dataclass


@dataclass
class NarrativeFactors:
    media: int
    social: int
    originality: int
    emotion: int
    momentum: int


class NarrativeConfidence:
    """
    Calculates the confidence score (0-100)
    for a narrative.
    """

    def calculate(self, factors: NarrativeFactors) -> int:
        score = (
            factors.media * 0.25
            + factors.social * 0.25
            + factors.originality * 0.20
            + factors.emotion * 0.15
            + factors.momentum * 0.15
        )

        return round(score)