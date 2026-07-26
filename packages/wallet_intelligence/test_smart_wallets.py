from packages.wallet_intelligence.profiler import update_wallet
from packages.wallet_intelligence.smart_wallets import detect_smart_wallets


# Simulate wallet history

update_wallet("wallet_1", 520)
update_wallet("wallet_1", 310)
update_wallet("wallet_1", 125)

update_wallet("wallet_2", 80)
update_wallet("wallet_2", 150)

update_wallet("wallet_3", -100, rugged=True)

wallets = [
    "wallet_1",
    "wallet_2",
    "wallet_3",
    "wallet_4"
]

result = detect_smart_wallets(wallets)

print("\nSMART MONEY REPORT")
print("=" * 40)

print("Smart Wallets:", result["count"])
print("Confidence Bonus:", result["confidence_bonus"])

print()

for wallet in result["wallets"]:

    print(wallet.address)
    print(wallet.grade)
    print(wallet.confidence)
    print()