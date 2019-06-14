import deeplabcut as dlc
import helpers

def extract(path_config_file, mode='automatic', algo="uniform"):
    # Set userfeedback to True if hoping to decide whether to extract frames on a video by video basis
    dlc.extract_frames(path_config_file, mode=mode, algo=algo, userfeedback=False, crop=False)

if __name__ == "__main__":
    path_config_file = helpers.get_config_path()
    extract(path_config_file, 'automatic', "uniform")
