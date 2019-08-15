import ctypes
import os
import json
import random

class ConfigReader:
    def __init__(self, config):
        self.config = config

    def read(self, key):
        return self.config[key] if self.config[key] is not None else self.config["default_values"][key]

    def change(self, key, value):
        self.config[key] = value

def get_video_full_paths(path_to_vidoes):
    # If filename[0] != "." since there might be hidden files
    full_paths = [os.path.normpath(os.path.join(os.getcwd(), path_to_vidoes, rel_path)) for rel_path in os.listdir(path_to_vidoes) if rel_path[0] != "."]
    return full_paths

def has_admin():
     return ctypes.windll.shell32.IsUserAnAdmin() != 0

def platform():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "Mac"
    elif platform == "win32":
        return "Windows"

def get_config_path():
    with open('config.json', 'r') as fp:
        config = json.load(fp)

    return config["path_config_file"]

def pick_random_videos(path, randomize=True):
    file_names = [name for name in os.listdir(path) if "ans" not in name and name[0] != "."]
    if randomize:
        random.shuffle(file_names)
    return file_names