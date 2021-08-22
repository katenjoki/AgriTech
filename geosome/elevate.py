from glob import glob
import rasterio
import geopandas as gpd
import shapely
from shapely.geometry import box
import requests
import urllib
import pandas as pd

def geo_shp(tif_path:str, shp_file_path:str) -> None:
    raster = rasterio.open(tif_path)
    bounds = raster.bounds

    df = gpd.GeoDataFrame({"id":1,"geometry":[box(*bounds)]})
   
    # save to file
    df.to_file(shp_file_path)
    print('Saved..')

#reference code https://gis.stackexchange.com/questions/338392/getting-elevation-for-multiple-lat-long-coordinates-in-python

def geo_elevation(shp_file_path:str) ->None:
    # USGS Elevation Point Query Service
    url = r'https://nationalmap.gov/epqs/pqs.php?'

    # generate points from geometry to get longitude and latitude
    df = gpd.read_file(shp_file_path)
    points = df.copy()
    points['point'] = points['geometry'].centroid
    df['latitude'] = points.point.y
    df['longitude'] = points.point.x 

    elevations = []
    for lat, lon in zip(df.latitude, df.longitude):
        # define rest query params
        params = {
            'output': 'json',
            'x': lon,
            'y': lat,
            'units': 'Meters'
        }

        # format query string and return query value
        result = requests.get((url + urllib.parse.urlencode(params)))
        elevations.append(result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])

    df['elevation(m)'] = elevations
    df.drop(['latitude','longitude'],axis=1,inplace=True)
    return df