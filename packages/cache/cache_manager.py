import json
import os
import time

CACHE_FILE = "packages/cache/intel_cache.json"

CACHE_DURATION = 300


def save_cache(data):

    payload = {
        "timestamp": time.time(),
        "data": data
    }

    with open(CACHE_FILE, "w") as f:
        json.dump(payload, f)


def load_cache():

    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE) as f:
        payload = json.load(f)

    age = time.time() - payload["timestamp"]

    if age > CACHE_DURATION:
        return None

    return payload["data"]