from app.engines.confidence_engine import ConfidenceEngine

engine = ConfidenceEngine()

token = {
    "liquidity_usd": 150000,
    "market_cap": 900000,
    "holders": 1700,
    "volume_24h": 600000,
    "buys": 320,
    "sells": 140,
}

print(engine.evaluate(token))