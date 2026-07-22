def build_wallet_profile(data):

    holders = data.get("holder", 0)

    largest_wallets = data.get("largest_wallets", [])

    whale_wallets = 0

    whale_supply = 0

    for wallet in largest_wallets:

        amount = float(wallet.get("uiAmount", 0))

        if amount >= 100000:
            whale_wallets += 1

        whale_supply += amount

    return {

        "holders": holders,

        "largest_wallets": len(largest_wallets),

        "whale_wallets": whale_wallets,

        "whale_supply": whale_supply,

        "wallet_growth": holders,

        "buy_volume": whale_supply,

        "sell_volume": 0,

        "buy_trades": whale_wallets,

        "sell_trades": 0,
    }