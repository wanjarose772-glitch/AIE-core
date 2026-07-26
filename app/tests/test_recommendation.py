from app.engines.recommendation_engine import RecommendationEngine
from app.engines.risk_engine import RiskResult
from app.engines.alpha_engine import AlphaResult
from app.engines.confidence_engine import ConfidenceResult


engine = RecommendationEngine()

risk = RiskResult(
    score=100,
    level="LOW",
    reasons=[]
)

alpha = AlphaResult(
    score=92,
    breakdown={}
)

confidence = ConfidenceResult(
    score=95,
    reasons=[]
)

result = engine.evaluate(
    risk,
    alpha,
    confidence
)

print(result)