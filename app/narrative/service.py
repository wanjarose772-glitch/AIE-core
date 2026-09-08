from dataclasses import dataclass

from app.narrative.confidence import (
    NarrativeConfidence,
    NarrativeFactors,
)

from app.narrative.scanner import NarrativeScanner


@dataclass
class Narrative:
    title: str
    category: str
    description: str
    score: int


class NarrativeService:

    def __init__(self):
        self.confidence = NarrativeConfidence()
        self.scanner = NarrativeScanner()

    def _score_story(self, title: str) -> int:

        scores = {

            "Jimothy": NarrativeFactors(
                media=98,
                social=96,
                originality=95,
                emotion=97,
                momentum=94,
            ),

            "Bumpy": NarrativeFactors(
                media=93,
                social=89,
                originality=94,
                emotion=98,
                momentum=90,
            ),

            "Punch": NarrativeFactors(
                media=88,
                social=84,
                originality=90,
                emotion=96,
                momentum=86,
            ),
        }

        return self.confidence.calculate(scores[title])

    def get_top_narratives(self):

        results = []

        for story in self.scanner.scan():

            results.append(

                Narrative(
                    title=story.title,
                    category=story.category,
                    description=story.description,
                    score=self._score_story(story.title),
                )

            )

        return results