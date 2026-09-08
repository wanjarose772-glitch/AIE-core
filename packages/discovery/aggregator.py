"""
Discovery Aggregator

Collects launches from all discovery sources,
filters them, normalizes them,
scores them and returns a ranked list.
"""

from packages.wallet_engine import WalletEngine
from packages.holder_engine import HolderEngine

from packages.intelligence.confidence import compute_confidence
from packages.metadata_engine.enricher import enrich_metadata
from packages.token_identity.resolver import resolve_identity

from packages.discovery.new_pairs import discover_new_pairs
from packages.discovery.geckoterminal import discover_gecko_launches
from packages.discovery.filters import filter_launches
from packages.discovery.scorer import score_launch
from packages.discovery.normalizer import normalize_token

from packages.scoring.conviction import compute_conviction


wallet_engine = WalletEngine()
holder_engine = HolderEngine()

def discover_all_launches():

    launches = []

    # -------------------------------------------------
    # DexScreener
    # -------------------------------------------------

    print("\nCollecting DexScreener launches...")
    launches.extend(discover_new_pairs())

    # -------------------------------------------------
    # GeckoTerminal
    # -------------------------------------------------

    print("\nCollecting GeckoTerminal launches...")
    launches.extend(discover_gecko_launches())

    print(f"\nTotal launches collected: {len(launches)}")

    if not launches:
        print("No launches returned from discovery sources.")
        return []

    # -------------------------------------------------
    # Filters
    # -------------------------------------------------

    print("\nFiltering launches...")
    launches = filter_launches(launches)

    print(f"After filters: {len(launches)}")

    ranked_tokens = []

    # -------------------------------------------------
    # Process Tokens
    # -------------------------------------------------

    for token in launches:

        try:

            print(f"\nProcessing {token.get('ticker', 'UNKNOWN')}")

            # -------------------------
            # Normalize
            # -------------------------

            token = normalize_token(token)

            # -------------------------
            # Metadata
            # -------------------------

            token = enrich_metadata(token)

            # -------------------------
            # Identity
            # -------------------------

            token = resolve_identity(token)

            # -------------------------
            # Discovery Score
            # -------------------------

            token = score_launch(token)

            # -------------------------
            # Wallet Engine
            # -------------------------

            print("Running Wallet Engine...")

            token = wallet_engine.analyze(token)
            token = holder_engine.analyze(token)

            print(
             f"Holder Score: {token.get('holder_score', 0)}"
            )
            print(
                f"Wallet Score: {token.get('wallet_score', 0)}"
            )

            # -------------------------
            # Conviction Score
            # -------------------------

            token = compute_conviction(token)

            # -------------------------
            # AIE Score
            # -------------------------

            token = compute_confidence(token)

            # -------------------------
            # Jupiter Link
            # -------------------------

            token["jupiter_url"] = (
                f"https://jup.ag/swap/SOL-{token['address']}"
            )

            print(
                f"✓ {token.get('ticker')} | "
                f"Discovery={token.get('discovery_score', 0)} | "
                f"Wallet={token.get('wallet_score', 0)} | "
                f"Conviction={token.get('conviction', 0)} | "
                f"AIE={token.get('aie_score', 0)}"
            )

            ranked_tokens.append(token)

        except Exception as e:

            print("\nERROR processing token")
            print(token.get("ticker", "UNKNOWN"))
            print(e)

    # -------------------------------------------------
    # Rank Results
    # -------------------------------------------------

    ranked_tokens.sort(
        key=lambda x: x.get("conviction", 0),
        reverse=True,
    )

    # -------------------------------------------------
    # Keep only Top 5
    # -------------------------------------------------

    ranked_tokens = ranked_tokens[:5]

    return ranked_tokens