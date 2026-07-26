from app.services.scanner import MarketScanner

scanner = MarketScanner()

tokens = scanner.scan()

print()

print(f"Found {len(tokens)} tokens")

print()

for token in tokens[:5]:

    print(token)

    print("-" * 60)