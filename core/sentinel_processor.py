# core/sentinel_processor.py

import rasterio
import numpy as np
from rasterio.mask import mask
from core.raster_utils import compute_ndvi


SCL_CLOUD_CLASSES = {3, 8, 9, 10, 11}  
# 3 = cloud_shadow, 8 = cloud_medium_prob, 9 = cloud_high_prob, 10 = thin_cirrus, 11 = snow


def load_and_clip(asset_url, geometry):
    """
    Loads a Sentinel-2 band and clips it to the AOI.
    """
    with rasterio.open(asset_url) as src:
        out, _ = mask(src, [geometry], crop=True)
    return out.squeeze()


def cloud_mask_scl(scl_arr):
    """
    Masks cloud pixels using SCL band.
    """
    mask_arr = np.isin(scl_arr, list(SCL_CLOUD_CLASSES))
    return mask_arr


def process_sentinel_item(item, aoi_geometry):
    """
    Given a STAC item (signed URL), compute NDVI:
    - Load B08 (NIR), B04 (RED)
    - Cloud mask using SCL band
    - Clip to AOI
    """

    assets = item["assets"]

    nir_url = assets["B08"]["href"]
    red_url = assets["B04"]["href"]
    scl_url = assets["SCL"]["href"]

    nir = load_and_clip(nir_url, aoi_geometry)
    red = load_and_clip(red_url, aoi_geometry)
    scl = load_and_clip(scl_url, aoi_geometry)

    cloud_mask = cloud_mask_scl(scl)

    ndvi = compute_ndvi(nir, red)
    ndvi[cloud_mask] = np.nan

    return ndvi