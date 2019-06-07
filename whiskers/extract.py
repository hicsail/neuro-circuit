import deeplabcut as dlc
import json

with open('config.json', 'r') as fp:
    config = json.load(fp)

path_config_file = config["path_config_file"]


dlc.extract_frames(path_config_file,'automatic', "uniform", crop=False)