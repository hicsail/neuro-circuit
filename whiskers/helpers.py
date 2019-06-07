import os

def get_video_full_path():
    video_list = []

    for filename in os.listdir(os.path.normpath(os.path.join(os.getcwd(), "./raw_videos"))):
        if filename[0] != ".":
            video_list.append(filename)

    cwd = os.getcwd()
    video_full_paths = [os.path.normpath(os.path.join(cwd, "./raw_videos", video)) for video in video_list]
    return video_full_paths