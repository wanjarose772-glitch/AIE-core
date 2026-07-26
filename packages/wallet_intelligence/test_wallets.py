from packages.wallet_intelligence.smart_wallets import SMART_WALLETS

print("=" * 60)
print("SMART WALLET DATABASE")
print("=" * 60)

print(f"\nLoaded {len(SMART_WALLETS)} wallets.\n")

for wallet in SMART_WALLETS:
    print(wallet)