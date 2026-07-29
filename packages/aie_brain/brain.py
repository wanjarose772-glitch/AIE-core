"""
AIE Brain

Coordinates every intelligence engine and produces
the final AIE decision for a token.
"""

from packages.score_engine.master_score import MasterScoreEngine


class AIEBrain:

    def __init__(self):
        self.master = MasterScoreEngine()

    def analyze(self, token: dict):

        # -----------------------------
        # Defaults
        # -----------------------------

        token.setdefault("discovery_score", 0)
        token.setdefault("alpha_score", 0)
        token.setdefault("wallet_score", 0)
        token.setdefault("whale_score", 0)
        token.setdefault("momentum", 0)
        token.setdefault("opportunity", 0)
        token.setdefault("trend", 0)
        token.setdefault("risk_score", 0)

        # -----------------------------
        # Final Score
        # -----------------------------

        result = self.master.calculate(token)

        token.update(result)

        return token