from packages.discovery.aggregator import discover_all_launches

launches = discover_all_launches()

print()
print("=" * 60)
print("DISCOVERY NETWORK")
print("=" * 60)

print(f"Total launches: {len(launches)}")
print()

for token in launches[:20]:
    print(token)