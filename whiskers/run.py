import deeplabcut as dlc
import os
cwd = os.getcwd()

task = 'whiskers' # Enter the name of your experiment Task
experimenter = 'sail' # Enter the name of the experimenter

# make full path here
video_list = ['./raw_videos/bb001_0_20180802092437.avi'] # Enter the paths of your videos you want to grab frames from.
video_full_path = [os.path.normpath(os.path.join(os.getcwd(), video)) for video in video_list]

path_config_file=dlc.create_new_project(task,experimenter,video_full_path, working_directory=os.getcwd(), copy_videos=False) #change the working directory to where you want the folders created.
print(path_config_file)

dlc.extract_frames(path_config_file,'automatic', "uniform", crop=False) #'uniform',
dlc.label_frames(path_config_file)
dlc.check_labels(path_config_file)

# add new videos
dlc.add_new_videos()

dlc.create_training_dataset(path_config_file)
dlc.train_network(path_config_file)