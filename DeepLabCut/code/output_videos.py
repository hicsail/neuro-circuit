import deeplabcut as dlc
import helpers

def output_videos(path_config_file, path_to_new_vidoes="../test_videos"):
    dlc.evaluate_network(path_config_file, plotting=False)
    full_paths = helpers.get_video_full_paths(path_to_new_vidoes)
    dlc.analyze_videos(path_config_file, full_paths)
    dlc.create_labeled_video(path_config_file, full_paths, save_frames=True, draw_skeleton=True)

if __name__ == "__main__":
    path_config_file = helpers.get_config_path()
    output_videos(path_config_file)