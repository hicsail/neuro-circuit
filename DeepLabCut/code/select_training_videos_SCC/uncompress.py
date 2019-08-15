import os
from pyunpack import Archive
for f in os.listdir("./"):
	Archive(f).extractall("../unzipped_videos/")