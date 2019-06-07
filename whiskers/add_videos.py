import deeplabcut as dlc
import json
import helpers

with open('config.json', 'r') as fp:
    config = json.load(fp)

path_config_file = config["path_config_file"]

# get full path here
video_full_paths = helpers.get_video_full_path()

dlc.add_new_videos(path_config_file, video_full_paths)