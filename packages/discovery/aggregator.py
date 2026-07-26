from packages.discovery.new_pairs import discover_new_pairs
from packages.discovery.geckoterminal import discover_gecko_launches

from packages.discovery.filters import filter_launches
from packages.discovery.scorer import score_launch
from packages.discovery.normalizer import normalize_token


def discover_all_launches():

    launches = []

    # ---------------------------------
    # DexScreener
    # ---------------------------------

    print("\nCollecting DexScreener launches...")
    launches.extend(discover_new_pairs())

    # ---------------------------------
    # GeckoTerminal
    # ---------------------------------

    print("\nCollecting GeckoTerminal launches...")
    launches.extend(discover_gecko_launches())

    # ---------------------------------
    # Early Filters
    # ---------------------------------

    print("\nFiltering launches...")
    launches = filter_launches(launches)

    # ---------------------------------
    # Discovery Score
    # ---------------------------------

    normalized = []

for token in launches:

    token = normalize_token(token)

    token = score_launch(token)

    normalized.append(token)

    launches = normalized

    launches.sort(
        key=lambda token: token["discovery_score"],
        reverse=True,
    )

     return launches