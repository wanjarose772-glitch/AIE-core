from packages.discovery.launch_scanner import discover_launches

tokens = discover_launches()

print()
print("=" * 60)
print("TODAY'S NEW LAUNCHES")
print("=" * 60)

for token in tokens:
    print(token)