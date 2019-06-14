import deeplabcut as dlc
import helpers
import extract
import os, json
from ruamel.yaml import YAML

def setup():
    # Check if having admin privilege if running Windows
    if helpers.platform() == "Windows" and helpers.has_admin() == False:
        print("Run with Administrative privilege for Windows")

    pre_config_yaml = YAML(typ='safe')
    with open("pre_config.yaml", 'r') as stream:
        pre_config = pre_config_yaml.load(stream)

    handle_none = helpers.ConfigReader(pre_config)
    task = handle_none.read("task")
    researchers = handle_none.read("researchers")
    # Get full path here
    video_full_paths = helpers.get_video_full_paths(pre_config["relative_Path_to_videos"])
    # Create projectp
    path_config_file = dlc.create_new_project(task, researchers, video_full_paths, working_directory=os.getcwd(), copy_videos=False)

    # Change the auto generated config file
    bodyparts = handle_none.read("bodyparts")
    numframes2pick = handle_none.read("numframes2pick")

    config_yaml = YAML()
    config_yaml.preserve_quotes = True
    with open(path_config_file, 'r') as stream:
        config = config_yaml.load(stream)

    config["bodyparts"] = bodyparts
    config["numframes2pick"] = numframes2pick

    with open(path_config_file, 'w') as fp:
        config_yaml.dump(config, fp)

    # Store the project path for future processes
    path_config = {"path_config_file" : path_config_file}

    frame_extraction_mode = handle_none.read("frame_extraction_mode")
    frame_extraction_algorithm = handle_none.read("frame_extraction_algorithm")

    extract.extract(path_config_file, mode=frame_extraction_mode, algo=frame_extraction_algorithm)

    with open('config.json', 'w') as fp:
        json.dump(path_config, fp, indent=4)

if __name__ == "__main__":
    setup()