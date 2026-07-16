from packages.data_sources.dexscreener import get_market_data
from packages.data_sources.birdeye import get_birdeye_data


def collect_market_data():
    """
    Collect market data from all configured sources.
    """

    market = []

    # Source 1: DexScreener
    market.extend(get_market_data())

    # Source 2: Birdeye
    birdeye = get_birdeye_data()

    # Birdeye returns {"tokens": [...]}
    if isinstance(birdeye, dict):
        market.extend(birdeye.get("tokens", []))

    return market