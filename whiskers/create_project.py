import deeplabcut as dlc
import os
import json

config = {}
task = 'whiskers' # Enter the name of your experiment Task
experimenter = 'sail' # Enter the name of the experimenter

# make full path here
video_list = []
config["video_list"] = []

for filename in os.listdir(os.path.normpath(os.path.join(os.getcwd(), "./raw_videos"))):
    video_list.append(filename)
    config["video_list"].append(filename)

cwd = os.getcwd()
video_full_path = [os.path.normpath(os.path.join(cwd, "./raw_videos", video)) for video in video_list]

# create project
path_config_file=dlc.create_new_project(task,experimenter,video_full_path, working_directory=cwd, copy_videos=False) #change the working directory to where you want the folders created.
config["path_config_file"] = path_config_file

with open('config.json', 'w') as fp:
    json.dump(config, fp, indent=4)