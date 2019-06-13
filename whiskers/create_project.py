import deeplabcut as dlc
import os
import json
import helpers

config = {}
task = 'whiskers' # Enter the name of your experiment Task
experimenter = 'sail' # Enter the name of the experimenter

# get full path here
video_full_paths = helpers.get_video_full_paths()
# create project
path_config_file=dlc.create_new_project(task,experimenter,video_full_paths, working_directory=os.getcwd(), copy_videos=False) #change the working directory to where you want the folders created.
config["path_config_file"] = path_config_file

with open('config.json', 'w') as fp:
    json.dump(config, fp, indent=4)