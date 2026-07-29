"""
Discovery Aggregator

Collects launches from all discovery sources,
filters them, normalizes them,
scores them and returns a ranked list.
"""

from packages.wallet_engine import WalletEngine
from packages.intelligence.confidence import compute_confidence

from packages.metadata_engine.enricher import enrich_metadata
from packages.token_identity.resolver import resolve_identity

from packages.discovery.new_pairs import discover_new_pairs
from packages.discovery.geckoterminal import discover_gecko_launches

from packages.discovery.filters import filter_launches
from packages.discovery.scorer import score_launch
from packages.discovery.normalizer import normalize_token


wallet_engine = WalletEngine()


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

    normalized = []

    # -------------------------------------------------
    # Process every token
    # -------------------------------------------------

    for token in launches:

        print(f"\nProcessing {token.get('ticker', 'UNKNOWN')}")

        try:

            # Normalize
            token = normalize_token(token)

            # Metadata
            token = enrich_metadata(token)

            # Identity
            token = resolve_identity(token)

            # Discovery Score
            token = score_launch(token)

            # Wallet Analysis
            print("Running Wallet Engine...")
            token = wallet_engine.analyze(token)


            print(
                f"Wallet Score: {token.get('wallet_score', 0)}"
            )

            token = compute_confidence(token)

            print(
                f"✓ {token.get('ticker')} | "
                f"Discovery={token.get('discovery_score', 0)} | "
                f"Wallet={token.get('wallet_score', 0)} | "
                f"AIE={token.get('aie_score', 0)}"
            )

            normalized.append(token)

        except Exception as e:

            print(f"ERROR processing token:")
            print(token.get("ticker"))
            print(e)

    # -------------------------------------------------
    # Sort Results
    # -------------------------------------------------

    normalized.sort(
        key=lambda x: x.get("discovery_score", 0),
        reverse=True,
    )

    return normalized