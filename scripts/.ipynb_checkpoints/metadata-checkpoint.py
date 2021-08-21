import json
import pdal
import pandas as pd
import urllib
from urllib.request import urlopen

CSV_PATH = "../data/data.csv"
JSON_PATH = "../data/cleaned.json"
PIPELINE_PATH = "../data/get_data.json"
        
def get_data(json_path:str,pipeline_path:str,csv_path:str):
    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)
    df = pd.read_csv(csv_path) 
    df = df[:500]
    for i in range(len(df)):
            
        OUTPUT_FILENAME_LAZ = "../laz/"+df.Region[i]+".laz"
        OUTPUT_FILENAME_TIF = "../tif/"+df.Region[i]+".tif"
            
        the_json['pipeline'][0]['bounds'] = df.Bounds[i]
        the_json['pipeline'][0]['filename'] = df.File_path[i]
        the_json['pipeline'][6]['filename'] = OUTPUT_FILENAME_LAZ
        the_json['pipeline'][7]['filename'] = OUTPUT_FILENAME_TIF
    
        pipeline = pdal.Pipeline(json.dumps(the_json))
    
        try:
            print('Successful')
            pipe_exec = pipeline.execute()
            metadata = pipeline.metadata
        except RuntimeError as e:
            print(e)
            print("RunTime Error, writing 0s and moving to next bounds")               

if __name__ == "__main__":
    get_data(JSON_PATH,PIPELINE_PATH,CSV_PATH)