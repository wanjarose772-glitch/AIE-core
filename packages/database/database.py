"""
AIE Memory Database

Stores previous token scans so AIE can compare
future scans against historical data.
"""

database = {}


def save_token(token: dict):

    database[token["address"]] = token


def get_token(address: str):

    return database.get(address)


def token_exists(address: str):

    return address in database


def all_tokens():

    return list(database.values())


def clear():

    database.clear()