"""
Whale Database
"""

from packages.whale_intelligence.whale_model import Whale


whale_db = {}


def get_whale(address: str) -> Whale:

    if address not in whale_db:

        whale_db[address] = Whale(address)

    return whale_db[address]


def save_whale(whale: Whale):

    whale_db[whale.address] = whale


def all_whales():

    return list(whale_db.values())