"""
Base provider interface for all AIE Narrative providers.

Every provider must implement the scan() method and return
a list of NarrativeStory objects.
"""

from abc import ABC, abstractmethod


class NarrativeProvider(ABC):

    @abstractmethod
    def scan(self):
        """
        Returns a list of NarrativeStory objects.
        """
        pass