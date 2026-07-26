from app.engines.risk_engine import RiskEngine

engine = RiskEngine()

token = {
    "liquidity_usd": 150000,
    "market_cap": 800000,
    "holders": 1800,
    "volume_24h": 950000,
    "buys": 520,
    "sells": 210,
}

result = engine.evaluate(token)

print(result)