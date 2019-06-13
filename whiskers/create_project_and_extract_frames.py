import deeplabcut as dlc
import os
import json
import helpers
import yaml
import extract

def setup():
    # Check if having admin privilege if running Windows
    if helpers.platform() == "Windows" and helpers.has_admin() == False:
        print("Run with Administrative privilege for Windows")

    with open("pre_config.yaml", 'r') as stream:
        pre_config = yaml.safe_load(stream)

    handle_none = helpers.Replacer(pre_config)
    task = handle_none.replace("task")
    researchers = handle_none.replace("researchers")
    # get full path here
    video_full_paths = helpers.get_video_full_paths(pre_config["relative_Path_to_videos"])
    # create project
    path_config_file=dlc.create_new_project(task, researchers, video_full_paths, working_directory=os.getcwd(), copy_videos=False)

    # store the project path for future processes
    config = {"path_config_file" : path_config_file}

    frame_extraction_mode = handle_none.replace("frame_extraction_mode")
    frame_extraction_algorithm = handle_none.replace("frame_extraction_algorithm")

    extract.extract(path_config_file, mode=frame_extraction_mode, algo=frame_extraction_algorithm)

    with open('config.json', 'w') as fp:
        json.dump(config, fp, indent=4)

if __name__ == "__main__":
    setup()

