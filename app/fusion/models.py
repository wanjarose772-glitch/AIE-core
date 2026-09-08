"""
AIE Fusion Models
"""

from dataclasses import dataclass, field


@dataclass
class EngineResult:

    engine: str

    score: int

    confidence: int

    recommendation: str

    reasoning: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)


@dataclass
class FusionInput:

    narrative: int

    liquidity: int

    momentum: int

    whales: int

    risk: int

    community: int