"""
AIE Narrative Normalizer

Responsible for cleaning and standardizing stories before
they enter the intelligence pipeline.
"""

from app.narrative.models import NarrativeStory


class NarrativeNormalizer:

    def normalize(self, stories: list[NarrativeStory]) -> list[NarrativeStory]:

        normalized = []

        for story in stories:

            story.title = story.title.strip().title()

            story.category = story.category.strip().title()

            story.description = story.description.strip()

            normalized.append(story)

        return normalized