"""
AIE Narrative Scanner

Acts as the orchestrator for all narrative providers.

Each provider returns NarrativeStory objects.

The scanner combines all provider results into a single list.
"""

from app.narrative.providers.news import NewsProvider


class NarrativeScanner:

    def __init__(self):

        self.providers = [
            NewsProvider(),
        ]

    def scan(self):

        stories = []

        for provider in self.providers:
            stories.extend(provider.scan())

        return stories