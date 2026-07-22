from packages.discovery.new_pairs import discover_new_pairs

pairs = discover_new_pairs()

print()
print("=" * 60)
print("FIRST FIVE NEW PAIRS")
print("=" * 60)

for pair in pairs[:5]:
    print(pair)