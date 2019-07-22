import deeplabcut as dlc
import helpers
import extract
import os, json
# a package that keeps the comments in yaml files
from ruamel.yaml import YAML

def setup():
    # Check if having admin privilege if running Windows
    if helpers.platform() == "Windows" and helpers.has_admin() == False:
        print("Run with Administrative privilege for Windows")
        # todo output something so that the batch script would terminate immediately
        return

    pre_config_handler = YAML(typ='safe')
    with open("../pre_config.yaml", 'r') as stream:
        pre_config = pre_config_handler.load(stream)

    none_handler = helpers.ConfigReader(pre_config)
    task = none_handler.read("task")
    researchers = none_handler.read("researchers")
    relative_path_to_working_directory = none_handler.read("relative_path_to_working_directory")
    # Get full path here
    video_full_paths = helpers.get_video_full_paths(pre_config["relative_path_to_videos"])
    # Create project
    path_config_file = dlc.create_new_project(task, researchers, video_full_paths, working_directory=relative_path_to_working_directory, copy_videos=False)

    # Store the project path for future processes
    path_config = {"path_config_file" : path_config_file}
    with open('./config.json', 'w+') as fp:
        json.dump(path_config, fp, indent=4)

    # Change the auto generated config file
    bodyparts = none_handler.read("bodyparts")
    numframes2pick = none_handler.read("numframes2pick")

    config_handler = YAML()
    config_handler.preserve_quotes = True
    with open(path_config_file, 'r') as stream:
        config = config_handler.load(stream)

    config["bodyparts"] = bodyparts
    config["numframes2pick"] = numframes2pick

    with open(path_config_file, 'w') as fp:
        config_handler.dump(config, fp)

    frame_extraction_mode = none_handler.read("frame_extraction_mode")
    frame_extraction_algorithm = none_handler.read("frame_extraction_algorithm")
    extract.extract(path_config_file, mode=frame_extraction_mode, algo=frame_extraction_algorithm)

if __name__ == "__main__":
    setup()