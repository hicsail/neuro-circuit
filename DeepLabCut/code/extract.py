import deeplabcut as dlc
import helpers
# a package that keeps the comments in yaml files
from ruamel.yaml import YAML

def extract(path_config_file):
    # Read configurations
    pre_config_handler = YAML(typ='safe')
    with open("../pre_config.yaml", 'r') as stream:
        pre_config = pre_config_handler.load(stream)

    none_handler = helpers.ConfigReader(pre_config)
    frame_extraction_mode = none_handler.read("frame_extraction_mode")
    frame_extraction_algorithm = none_handler.read("frame_extraction_algorithm")

    # Set userfeedback to True if hoping to decide whether to extract frames on a video by video basis
    dlc.extract_frames(path_config_file, mode=frame_extraction_mode, algo=frame_extraction_algorithm, userfeedback=False, crop=False)

if __name__ == "__main__":
    path_config_file = helpers.get_config_path()
    extract(path_config_file)
