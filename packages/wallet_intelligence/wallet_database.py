"""
Wallet Database
"""

from packages.wallet_intelligence.wallet_model import Wallet


wallet_db = {}


def get_wallet(address):

    if address not in wallet_db:

        wallet_db[address] = Wallet(address)

    return wallet_db[address]


def save_wallet(wallet):

    wallet_db[wallet.address] = wallet


def all_wallets():

    return list(wallet_db.values())