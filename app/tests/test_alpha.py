from app.engines.alpha_engine import AlphaEngine

engine = AlphaEngine()

token = {
    "liquidity_usd": 200000,
    "market_cap": 900000,
    "holders": 2400,
    "volume_24h": 700000,
    "buys": 550,
    "sells": 180,
}

result = engine.evaluate(token)

print(result)