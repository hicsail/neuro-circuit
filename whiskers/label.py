import deeplabcut as dlc
import helpers

def label(path_config_file):
    dlc.label_frames(path_config_file)
    dlc.check_labels(path_config_file)

if __name__ == "__main__":
    path_config_file = helpers.get_config_path()
    label(path_config_file)