from packages.discovery.pumpfun import discover_new_launches

coins = discover_new_launches()

print()

print("=" * 60)
print("FIRST TEN PUMP.FUN TOKENS")
print("=" * 60)

for coin in coins[:10]:
    print(coin)