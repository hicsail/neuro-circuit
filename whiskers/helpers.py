import ctypes
import os

class Replacer:
    def __init__(self, pre_config):
        self.pre_config = pre_config

    def replace(self, key):
        return self.pre_config[key] if self.pre_config[key] is not None else self.pre_config["default_values"][key]

def get_video_full_paths(path_to_vidoes):
    # if filename[0] != "." since there might be hidden files
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