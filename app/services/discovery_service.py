"""
AIE Discovery Service

Runs the complete AIE pipeline.
"""

from packages.discovery.aggregator import discover_all_launches
from packages.aie_brain.brain import AIEBrain


class DiscoveryService:

    def __init__(self):
        self.brain = AIEBrain()

    def intel(self):

        launches = discover_all_launches()

        analyzed = []

        for token in launches:
            analyzed.append(
                self.brain.analyze(token)
            )

        analyzed.sort(
            key=lambda x: x["aie_score"],
            reverse=True,
        )

        return analyzed