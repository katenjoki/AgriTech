from glob import glob
import rasterio
import geopandas as gpd
import shapely
from shapely.geometry import box
import requests
import urllib
import pandas as pd

'''def geo_shp(tif_path:str, shp_file_path:str) -> None:
    raster = rasterio.open(tif_path)
    bounds = raster.bounds

    df = gpd.GeoDataFrame({"id":1,"geometry":[box(*bounds)]})
   
    # save to file
    df.to_file(shp_file_path)
    print('Saved..')'''

#reference code https://gis.stackexchange.com/questions/338392/getting-elevation-for-multiple-lat-long-coordinates-in-python

def geo_elevation(shp_file_path:str) ->None:
    gdf = gpd.read_file(shp_file_path)
    gdf.rename(columns={'Z':'elevation'},inplace=True)
    return gdf
