from app.collectors.dexscreener import DexScreenerCollector

collector = DexScreenerCollector()

pairs = collector.search("SOL")

print(f"Pairs found: {len(pairs)}")

if pairs:
    print()
    print("First Pair")
    print("----------------")

    pair = pairs[0]

    print(pair.get("baseToken", {}).get("symbol"))
    print(pair.get("priceUsd"))
    print(pair.get("liquidity"))