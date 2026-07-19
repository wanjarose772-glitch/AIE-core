from packages.oracle.intel import enrich
from packages.hawk.discovery import fetch_new_launches
from packages.hawk.filters import safety_filter
from packages.hawk.scoring import calculate_alpha


def discover_new_tokens():

    launches = fetch_new_launches()

    safe_tokens = safety_filter(launches)

    for token in safe_tokens:

        token = enrich(token)

        result = calculate_alpha(token)

        token.update(result)

    return safe_tokens