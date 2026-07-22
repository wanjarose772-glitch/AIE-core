from packages.discovery.new_pairs import discover_new_pairs

pairs = discover_new_pairs()

print()
print("FIRST FIVE")
print("-" * 40)

for pair in pairs[:5]:
    print(pair)