from packages.discovery.live_pairs import discover_live_pairs

pairs = discover_live_pairs()

print()

print("=" * 60)
print("TOP CANDIDATES")
print("=" * 60)

for pair in pairs[:20]:
    print(pair)