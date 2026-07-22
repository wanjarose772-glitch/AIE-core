from packages.wallet_intelligence.smart_wallets import analyze_wallets

token = {
    "address": "GK1EPJoR4bHRDhzoS8qZAS4FaAfn4bjHyGmqiaAYJoty"
}

result = analyze_wallets(token)

print(result)