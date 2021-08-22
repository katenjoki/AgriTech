import json
import pdal
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
    
    raster = rasterio.open(output_tif)
    bounds = raster.bounds

    df = geopandas.GeoDataFrame({"id":1,"geometry":[box(*bounds)]})
   
    # save to file
    df.to_file(output_shp)
    print('Saved..')