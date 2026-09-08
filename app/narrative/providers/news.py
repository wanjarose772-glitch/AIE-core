"""
AIE News Provider

Mock implementation.

Later:
- NewsAPI
- Google News
- RSS
"""

from app.narrative.models import NarrativeStory
from app.narrative.providers.base import NarrativeProvider


class NewsProvider(NarrativeProvider):

    def scan(self):

        return [

            NarrativeStory(
                title="Jimothy",
                category="Animal",
                description="Seattle raccoon becoming an internet icon.",
                source="News",
                sentiment=0.97,
                engagement=125000,
            ),

            NarrativeStory(
                title="Bumpy",
                category="Animal",
                description="Orphaned baby hippo gaining worldwide attention.",
                source="News",
                sentiment=0.95,
                engagement=97000,
            ),

            NarrativeStory(
                title="Punch",
                category="Animal",
                description="Rescued monkey with a growing emotional community.",
                source="News",
                sentiment=0.91,
                engagement=81000,
            ),

        ]