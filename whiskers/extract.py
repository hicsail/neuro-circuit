import deeplabcut as dlc
import json

def extract(path_config_file, mode='automatic', algo="uniform"):
    # set userfeedback to True if hoping to decide whether to extract frames on a video by video basis
    dlc.extract_frames(path_config_file, mode=mode, algo=algo, userfeedback=False, crop=False)

if __name__ == "__main__":
    with open('config.json', 'r') as fp:
        config = json.load(fp)

    path_config_file = config["path_config_file"]
    extract(path_config_file, 'automatic', "uniform")
