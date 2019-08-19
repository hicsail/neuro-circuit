import deeplabcut as dlc
import helpers

def train(path_config_file):
    dlc.create_training_dataset(path_config_file)
    dlc.train_network(path_config_file, shuffle=1, saveiters=15, displayiters=3)

if __name__ == "__main__":
    path_config_file = helpers.get_config_path()
    train(path_config_file)