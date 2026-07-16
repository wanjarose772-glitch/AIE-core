def detect_new_listing(ticker, previous_tokens):

    if ticker not in previous_tokens:
        return True

    return False


def listing_status(is_new):

    if is_new:
        return "🆕 NEW LISTING"

    return ""