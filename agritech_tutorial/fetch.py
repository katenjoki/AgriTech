import json
import pdal
from osgeo import gdal, ogr
import numpy as np
import rasterio
from glob import glob
import geopandas as gpd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
PIPELINE_PATH = "get_data.json"

def geo_fetch(bounds:gpd.GeoDataFrame,region:str,data_path:str=DATA_PATH,pipeline_path:str=PIPELINE_PATH):
    #boundaries = bounds.to_crs(epsg=3857)
    Xmin,ymin,Xmax,ymax = bounds.total_bounds
    access_path = data_path + region + "ept.json"
    r = region.strip('/')
    output_laz = "../files/laz/" + r + ".laz"
    output_tif = "../files/tif/" + r + ".tif"
    filename = "../files/shp/" + r
    #generating the shapefile
    #code referenced from https://gis.stackexchange.com/questions/268395/converting-raster-tif-to-point-shapefile-using-python
# The GeoTIFF was first converted into the XYZ format then the .xyz file was renamed to .csv and finally to ESRI Shapefile.

    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)

    the_json['pipeline'][0]['bounds'] = f"([{Xmin},{Xmax}],[{ymin},{ymax}])"
    the_json['pipeline'][0]['filename'] = access_path
    the_json['pipeline'][5]['filename'] = output_laz
    the_json['pipeline'][6]['filename'] = output_tif

    pipeline = pdal.Pipeline(json.dumps(the_json))

    try:
        pipe_exec = pipeline.execute()
        metadata = pipeline.metadata

    except RuntimeError as e:
        print(e)
        print("RunTime Error, writing 0s and moving to next bounds")
        
    #inDs = gdal.Open('{}.tif'.format(filename))
    inDs = gdal.Open(output_tif)
    outDs = gdal.Translate('{}.xyz'.format(filename), inDs, format='XYZ', creationOptions=["ADD_HEADER_LINE=YES"])
    outDs = None
    try:
        os.remove('{}.csv'.format(filename))
    except OSError:
            pass
    os.rename('{}.xyz'.format(filename), '{}.csv'.format(filename))
    os.system('ogr2ogr -f "ESRI Shapefile" -oo X_POSSIBLE_NAMES=X* -oo Y_POSSIBLE_NAMES=Y* -oo KEEP_GEOM_COLUMNS=NO {0}.shp {0}.csv'.format(filename))
    output_shp = filename + '.shp'

    gdf = gpd.read_file(output_shp)
    gdf.rename(columns={'Z':'elevation'},inplace=True)
    return gdf

def geo_plot(gdf:gpd.GeoDataFrame)->None:
    fig = plt.figure(figsize=(15,6))
    ax = plt.axes(projection='3d')
    ax.scatter3D(gdf.geometry.x, gdf.geometry.y, gdf.elevation, c=gdf.elevation, cmap='terrain')
    ax.set_xlabel("Longitude")
    ax.set_xlabel("Latitude")
    ax.set_zlabel("Elevation")
    plt.savefig("../files/terrain.png")
    plt.show()