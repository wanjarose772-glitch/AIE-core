"""
AIE Core

Central intelligence engine for AIE.

Every discovered token passes through each analysis
engine before a final intelligence report is returned.
"""

from packages.score_engine.master_score import MasterScoreEngine

from app.engines.alpha_engine import AlphaEngine
from app.engines.risk_engine import RiskEngine
from app.engines.confidence_engine import ConfidenceEngine
from app.engines.recommendation_engine import RecommendationEngine

from app.engines.momentum_engine import MomentumEngine
from app.engines.opportunity_engine import OpportunityEngine
from app.engines.conviction_engine import ConvictionEngine
from app.engines.trend_engine import TrendEngine

from packages.wallet_intelligence.wallet_tracker import WalletTracker
from packages.whale_intelligence.whale_tracker import WhaleTracker


class AIECore:

    def __init__(self):

        self.alpha = AlphaEngine()
        self.risk = RiskEngine()
        self.confidence = ConfidenceEngine()
        self.recommendation = RecommendationEngine()

        self.momentum = MomentumEngine()
        self.opportunity = OpportunityEngine()
        self.conviction = ConvictionEngine()
        self.trend = TrendEngine()

        self.wallets = WalletTracker()
        self.whales = WhaleTracker()

        self.master_score = MasterScoreEngine()

    def analyze(self, token):

        # ---------------------------------
        # Core Engines
        # ---------------------------------

        alpha = self.alpha.analyze(token)

        risk = self.risk.analyze(token)

        confidence = self.confidence.analyze(
            token,
            alpha,
            risk,
        )

        recommendation = self.recommendation.analyze(
            alpha,
            risk,
        )

        # ---------------------------------
        # Intelligence Engines
        # ---------------------------------

        momentum = self.momentum.analyze(token)

        opportunity = self.opportunity.analyze(token)

        token["alpha"] = alpha.score

        trend = self.trend.analyze(token)

        conviction = self.conviction.analyze(
            alpha,
            momentum,
            opportunity,
            confidence,
            risk,
        )

        # ---------------------------------
        # Smart Money
        # ---------------------------------

        wallets = self.wallets.process_token(token)
        whales = self.whales.process_token(token)

        # WalletTracker currently returns a LIST
        if isinstance(wallets, list):
            wallet_score = len(wallets) * 10
        elif isinstance(wallets, dict):
            wallet_score = wallets.get("score", 0)
        else:
            wallet_score = 0

        # WhaleTracker currently returns a LIST
        if isinstance(whales, list):
            whale_score = len(whales) * 10
        elif isinstance(whales, dict):
            whale_score = whales.get("score", 0)
        else:
            whale_score = 0

        # ---------------------------------
        # Master Score
        # ---------------------------------

        master_score = self.master_score.calculate({

            "discovery_score": token.get(
                "discovery_score",
                0,
            ),

            "alpha_score": alpha.score,

            "risk_score": getattr(
                risk,
                "score",
                0,
            ),

            "momentum": momentum.score,

            "opportunity": opportunity.score,

            "trend": trend.score,

            "wallet_score": wallet_score,

            "whale_score": whale_score,

        })

        # ---------------------------------
        # Final Response
        # ---------------------------------

        return {

            "alpha": alpha,

            "risk": risk,

            "confidence": confidence,

            "recommendation": recommendation,

            "momentum": momentum,

            "opportunity": opportunity,

            "conviction": conviction,

            "trend": trend,

            "wallets": wallets,

            "whales": whales,

            "master_score": master_score,

        }