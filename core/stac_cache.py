# core/stac_cache.py

import hashlib
import json
import os
from config import CACHE_DIR


def hash_query(query: dict):
    query_str = json.dumps(query, sort_keys=True)
    return hashlib.md5(query_str.encode()).hexdigest()


def cache_exists(key):
    return os.path.exists(os.path.join(CACHE_DIR, key + ".json"))


def save_cache(key, data):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, key + ".json")
    with open(path, "w") as fp:
        json.dump(data, fp)
    return True


def load_cache(key):
    path = os.path.join(CACHE_DIR, key + ".json")
    with open(path, "r") as fp:
        return json.load(fp)