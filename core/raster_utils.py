# core/raster_utils.py

import rasterio
from rasterio.mask import mask
import numpy as np


def read_and_clip(asset_url, geometry):
    """
    Loads a raster band and clips to AOI geometry.
    """
    with rasterio.open(asset_url) as src:
        out, _ = mask(src, [geometry], crop=True)
    return out.squeeze()


def compute_ndvi(nir, red):
    """
    NDVI calculation with small constant for division stability.
    """
    ndvi = (nir - red) / (nir + red + 1e-6)
    return np.clip(ndvi, -1, 1)


def remove_outliers(arr, threshold=3):
    """
    Removes NDVI outliers using Z-score method.
    """
    mean = np.nanmean(arr)
    std = np.nanstd(arr)
    z = (arr - mean) / (std + 1e-6)
    return np.where(np.abs(z) < threshold, arr, np.nan)