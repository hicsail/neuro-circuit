import os
import random
import shutil
import zipfile
from ruamel.yaml import YAML
from pyunpack import Archive
from shutil import copyfile

def load_config():
    config_handler = YAML(typ='safe')
    with open("./config.yaml", 'r', encoding="utf-8") as stream:
        config = config_handler.load(stream)
    return config

def get_file_names(path, randomize=True):
    level_1_paths = [name for name in os.listdir(path) if name[0] != "."]
    if randomize:
        random.shuffle(file_names)
    return file_names

config = load_config()
total_videos = config["total_videos"]
frames_per_video = config["frames_per_video"]
dir = config["videos_dir"]

file_names = [os.path.join(path, filename)
         for path, dirs, files in os.walk(dir)
         for filename in files
         ]

# list is shuffled in place
random.shuffle(file_names)

for i in range(total_videos):
	file_name = file_names[i]
	actual_name = file_name.split("/")[-1]
	copyfile(f"{file_name}", f"./_selected_zip_files/{actual_name}")
	#Archive(f"./selected_videos/{actual_name}").extractall("./unzipped_videos/")

import os
from pyunpack import Archive
for f in os.listdir("./"):
	Archive(f).extractall("../unzipped_videos/")