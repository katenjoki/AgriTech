import json
import pdal
PIPELINE_PATH = "get_data.json"
USGS_PATH = "..data/data_usgs.json"
def get_raster_terrain(pipeline_path:str,usgs_path):
    with (open(pipeline_path) as json_file,
         open(usgs_path) as json_usgs
         ):
        the_json = json.load(json_file)
        the_usgs = json.load(json_usgs)
        
        with open(json_path,"w") as json_file:
        json.dump(geo_dict,json_file)                 

if __name__ == "__main__":
    get_data(DATASET_PATH,JSON_PATH)