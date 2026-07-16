from packages.pipeline.market_pipeline import run_pipeline


def get_watchlist():
    """
    Return the current AIE watchlist.
    """
    return run_pipeline()