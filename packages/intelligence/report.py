import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

HELIUS_URL = (
    f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"
)

from packages.data_sources.birdeye import (
    get_trending_tokens,
    get_token_overview,
)

from packages.data_sources.birdeye_transactions import (
    get_token_transactions,
)

from packages.wallet_intelligence.collector import (
    collect_wallet_data,
)

from packages.intelligence.analyzer import (
    analyze_token,
)

from packages.cache.cache_manager import (
    save_cache,
    load_cache,
)

from packages.config.settings import (
    EXCLUDED_TICKERS,
)


def build_intelligence_report():

    # -----------------------------------
    # Cache
    # -----------------------------------

    cached = load_cache()

    if cached:
        print("Using cached intelligence report...")
        return cached

    report = []

    tokens = get_trending_tokens()

    if not tokens:
        return []

    # -----------------------------------
    # Scan tokens
    # -----------------------------------

    for item in tokens:

        token = {
            "ticker": item.get("symbol"),
            "name": item.get("name"),
            "chain": "solana",
            "price": item.get("price"),
            "liquidity": item.get("liquidity"),
            "volume": item.get("volume24hUSD"),
            "market_cap": item.get("mc"),
            "address": item.get("address"),
            "source": "Birdeye",
        }

        # -----------------------------------
        # Skip major coins
        # -----------------------------------

        if token["ticker"] in EXCLUDED_TICKERS:
            print(f"Skipping {token['ticker']}")
            continue

        print(f"\nAnalyzing {token['ticker']}")

        # -----------------------------------
        # Metadata
        # -----------------------------------

        metadata = get_token_overview(
            token["address"]
        )

        # -----------------------------------
        # Transactions
        # -----------------------------------

        transaction_data = get_token_transactions(
            token["address"]
        )

        if transaction_data is None:
            print("No transaction data.")
            continue

        # -----------------------------------
        # Wallet Intelligence
        # -----------------------------------

        wallet_data = collect_wallet_data(
            token["address"]
        )

        token = analyze_token(
            token,
            metadata,
            transaction_data,
            wallet_data,
        )
        print(
    f"{token['ticker']} | "
    f"Alpha={token.get('alpha_score')} | "
    f"Confidence={token.get('confidence')}%"
)

        report.append(token)

        # -----------------------------------
        # Development Limit
        # -----------------------------------

        if len(report) >= 10:
            break

    save_cache(report)

    return report