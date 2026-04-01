# core/vector_utils.py

import geopandas as gpd
from shapely.geometry import mapping


def load_aoi_geojson(aoi_path_or_name):
    """
    Loads AOI from:
    - Local GeoJSON path
    - Local shapefile
    - Predefined AOI lookup
    """

    # Example predefined regions
    predefined = {
        "Bengaluru Rural": "data/aoi/bengaluru_rural.geojson",
        "Karnataka": "data/aoi/karnataka.geojson"
    }

    if aoi_path_or_name in predefined:
        gdf = gpd.read_file(predefined[aoi_path_or_name])
    else:
        gdf = gpd.read_file(aoi_path_or_name)

    return mapping(gdf.to_crs(4326).geometry[0])


def load_aoi_geometry(aoi_path_or_name):
    """
    Returns geometry object (not GeoJSON mapping)
    """
    predefined = {
        "Bengaluru Rural": "data/aoi/bengaluru_rural.geojson"
    }

    file = predefined.get(aoi_path_or_name, aoi_path_or_name)
    gdf = gpd.read_file(file)
    return gdf.to_crs(4326).geometry[0]