import json
import pdal
import gdal
import numpy as np
import rasterio
from glob import glob
import shapely
from shapely.geometry import box
import geopandas

DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
PIPELINE_PATH = "geosome/data/get_data.json"

def geo_fetch(bounds:str,region:str,data_path:str=DATA_PATH,pipeline_path:str=PIPELINE_PATH):
    access_path = data_path + region + "ept.json"
    r = region.strip('/')
    output_laz = "geosome/laz/" + r + ".laz"
    output_tif = "geosome/tif/" + r + ".tif"
    output_shp = "geosome/shp/" + r + ".shp"
    
    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)

    the_json['pipeline'][0]['bounds'] = bounds
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
        
    #source of code for elevations https://www.earthdatascience.org/tutorials/visualize-digital-elevation-model-contours-matplotlib/ 
    #get elevations
    filename = output_tif
    gdal_data = gdal.Open(filename)
    gdal_band = gdal_data.GetRasterBand(1)
    nodataval = gdal_band.GetNoDataValue()

    # convert elevations to numpy array
    data_array = gdal_data.ReadAsArray().astype(np.float)
    data_array

    # replace missing values if necessary
    if np.any(data_array == nodataval):
        data_array[data_array == nodataval] = np.nan