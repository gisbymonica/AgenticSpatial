# agents/processing_agent.py

import numpy as np
from core.sentinel_processor import process_sentinel_item
from core.vector_utils import load_aoi_geometry


def generate_ndvi_timeseries(items, task):
    """
    Processes a list of STAC items to produce:
    - time_list (list of datetimes)
    - ndvi_means (list of mean NDVI per timestep)
    """

    aoi_geometry = load_aoi_geometry(task["aoi"])

    ndvi_means = []
    time_list = []

    for item in items:
        try:
            ndvi = process_sentinel_item(item, aoi_geometry)
            ndvi_means.append(float(np.nanmean(ndvi)))
            time_list.append(item["properties"]["datetime"][:10])
        except Exception as e:
            print("Error processing item:", e)

    return time_list, ndvi_means
