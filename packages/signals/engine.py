from packages.signals.liquidity import liquidity_signal
from packages.signals.volume import volume_signal


def generate_signals(change):

    return {

        "liquidity_signal":
            liquidity_signal(
                change["liquidity_change"]
            ),

        "volume_signal":
            volume_signal(
                change["volume_change"]
            )

    }