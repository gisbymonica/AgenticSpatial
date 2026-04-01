# agents/dataset_agent.py

import json
from datetime import datetime
from pystac_client import Client
import planetary_computer as pc
from core.vector_utils import load_aoi_geojson
from config import STAC_ENDPOINT
from core.stac_cache import hash_query, cache_exists, load_cache, save_cache



def fetch_sentinel_series(task):
    

    

    return signed_items


def fetch_sentinel_series(task):
    """
    Fetch Sentinel-2 STAC items based on:
    - AOI geometry
    - Date range
    - Cloud cover filter
    """
    q_hash = hash_query(task)

    if cache_exists(q_hash):
        return load_cache(q_hash)

    aoi_geojson = load_aoi_geojson(task["aoi"])
    start_date = task["date_range"]["start"]
    end_date = task["date_range"]["end"]

    client = Client.open(STAC_ENDPOINT)

    search = client.search(
        collections=["sentinel-2-l2a"],
        intersects=aoi_geojson,
        datetime=f"{start_date}/{end_date}",
        query={"eo:cloud_cover": {"lt": 20}},
        limit=100
    )

    items = list(search.get_items())
    print(f"Found {len(items)} Sentinel scenes before signing URLs.")

    # Sign for direct blob access (Planetary Computer)
    signed_items = [pc.sign(item).to_dict() for item in items]

    save_cache(q_hash, signed_items)
    return signed_items