import pdal
import json

DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/" #lidar path
REGION = 'USGS LPC CO SoPlatteRiver Lot5 2013 LAS 2015/'
BOUNDS = "([-11669524.7, -11666600.8], [4776607.3, 4778714.4])"
ACCESS_PATH = DATA_PATH + REGION + "ept.json"
OUTPUT_FILENAME_LAZ = "laz/SoPlatterRiver.laz"
OUTPUT_FILENAME_TIF = "tif/SoPlatterRiver.tif"
PIPELINE_PATH = "get_data.json"

def get_raster_terrain(bounds:str, region:str, access_path:str = ACCESS_PATH, output_filename_laz:str = OUTPUT_FILENAME_LAZ,
                      output_filename_tif:str = OUTPUT_FILENAME_TIF, pipeline_path:str = PIPELINE_PATH)->None:
    
    with open(PIPELINE_PATH) as json_file:
        the_json = json.load(json_file)
        
    the_json['pipeline'][0]['bounds'] = bounds
    the_json['pipeline'][0]['filename'] = ACCESS_PATH
    the_json['pipeline'][3]['filename'] = OUTPUT_FILENAME_LAZ
    the_json['pipeline'][4]['filename'] = OUTPUT_FILENAME_TIF
    
    pipeline = pdal.Pipeline(json.dumps(the_json))
    
    try:
        
        pipe_exec = pipeline.execute()
        metadata = pipeline.metadata
        
    except RuntimeError as e:
        print(e)
        print("RunTime Error, writing 0s and moving to next bounds")

if __name__ == "__main__":
    get_raster_terrain(bounds=BOUNDS, region=REGION)