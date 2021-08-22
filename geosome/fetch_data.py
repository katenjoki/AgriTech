import json
import urllib
from urllib.request import urlopen

DATASET_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
JSON_PATH = "../data/data_usgs.json"
        
def get_data(dataset_path:str,json_path:str):
    geo_dict = {'Region':[],
                'File_path':[],
                'Bounds':[]
                }
    with open('../filename.txt') as filenames:
        for f in filenames:
            f = f.strip('\n')
            geo_dict['Region'].append(f)
            file = dataset_path + f +"ept.json"
            geo_dict['File_path'].append(file)
            try:
                meta = json.load(urlopen(file))
                bounds = meta["bounds"]
            except:
                bounds = None                            
            geo_dict['Bounds'].append(bounds)    
            
            
    with open(json_path,"w") as json_file:
        json.dump(geo_dict,json_file)                 

if __name__ == "__main__":
    get_data(DATASET_PATH,JSON_PATH)