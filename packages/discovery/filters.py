def filter_launches(launches):

    filtered = []

    for token in launches:

        liquidity = token.get("liquidity", 0)

        volume = token.get("volume", 0)

        # Minimum liquidity
        if liquidity < 500:
            continue

        # Ignore completely dead pools
        if volume < 10:
            continue

        filtered.append(token)

    return filtered