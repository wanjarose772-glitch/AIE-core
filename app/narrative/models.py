"""
AIE Narrative Models

Shared data models used throughout the Narrative Intelligence Engine.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class NarrativeStory:
    """
    Standard narrative object returned by every provider.
    """

    title: str
    category: str
    description: str

    source: str

    url: str = ""

    published_at: datetime | None = None

    keywords: list[str] = field(default_factory=list)

    sentiment: float = 0.0

    engagement: int = 0

    confidence: int = 0