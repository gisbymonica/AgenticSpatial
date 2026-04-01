from pystac_client import Client
import planetary_computer as pc

def search_sentinel2(aoi_geojson, start_date, end_date):
    client = Client.open("https://planetarycomputer.microsoft.com/api/stac/v1/")

    search = client.search(
        collections=["sentinel-2-l2a"],
        intersects=aoi_geojson,
        datetime=f"{start_date}/{end_date}"
    )

    items = list(search.get_items())
    signed = [pc.sign(item).to_dict() for item in items]
    return signed