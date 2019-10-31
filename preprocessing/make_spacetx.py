import os
import argparse
import time
import tifffile
from tqdm import tqdm
from skimage import io
from slicedimage import ImageFormat
from starfish.experiment.builder import write_experiment_json

from tile_wrapper import ImageTileFetcher

# We assume these constants will not differ between rounds and samples
STITCHED_DIR = "02_Stitched"
SPACE_TX_DIR = "SpaceTxFormat"
ORIGINAL = "original"
FORMATTED = "formatted"

All_CHANNELS = ['488', '561', 'Cy5', 'Cy7']
FOV_NUM = 1

if __name__ == "__main__":
	# parse inputs
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_dir", "-i", help="directory of the sample")
	parser.add_argument("--round", "-r", help="number of round")
	parser.add_argument("--sample", "-s", help="number of sample")

	args = parser.parse_args()
	SAMPLE_DIR = args.input_dir
	ROUND_NUM = args.round.zfill(2)
	SAMPLE_NUM = args.sample

	# parse channel names from the directory itself
	CHANNELS = [name for name in os.listdir(SAMPLE_DIR) if name in All_CHANNELS]
	CHANNEL_NUM = len(CHANNELS)
	print(f"Channels in this sample: {CHANNELS}")

	# we assume the stitched images follow the RrrSs_ccc.tif format
	# where rr is the round number, s is the sample number, and ccc is the channel name
	# e.g. R05S2_561
	BASE_NAME = f"R{ROUND_NUM}S{SAMPLE_NUM}"
	STITCHED_FILES = [f"{BASE_NAME}_{ch}.tif" for ch in CHANNELS]
	print(f"Stitched images in sample: {STITCHED_FILES}")

	# make sure the files are in the right directory and named properly
	# fail early if this is incorrect
	for channel_num, channel_name in enumerate(CHANNELS):
		if not os.path.exists(os.path.join(SAMPLE_DIR, channel_name, STITCHED_DIR, STITCHED_FILES[channel_num])):
			raise FileNotFoundError(f"{STITCHED_FILES[channel_num]} does not exist. Are you sure it is named correctly?")

	# make SpaceTxFormat\original and SpaceTxFormat\formatted folders
	TX_ORIGINAL_DIR = os.path.join(SAMPLE_DIR, SPACE_TX_DIR, ORIGINAL)
	os.makedirs(TX_ORIGINAL_DIR)
	assert os.path.exists(TX_ORIGINAL_DIR)

	TX_FORMATTED_DIR = os.path.join(SAMPLE_DIR, SPACE_TX_DIR, FORMATTED)
	os.makedirs(TX_FORMATTED_DIR)
	assert os.path.exists(TX_FORMATTED_DIR)

	# Load all stitched images in the sample and split by Z slice per image
	# write all Z stacks to the SpaceTxFormat\original folder
	for channel_num, channel_name in tqdm(enumerate(CHANNELS)):
		start_time = time.time()

		STITCHED_FILE = os.path.join(SAMPLE_DIR, channel_name, STITCHED_DIR, STITCHED_FILES[channel_num])
		stitched_img = tifffile.imread(STITCHED_FILE)
		print(f"Time to read image {STITCHED_FILE}:" + str(time.time() - start_time))

		Z_NUM = stitched_img.shape[0]
		for z in range(Z_NUM):
			Z_FILE_NAME = f"{BASE_NAME}_CH{channel_num}_Z{z+1:03}.tif"
			Z_FILE = os.path.join(TX_ORIGINAL_DIR, Z_FILE_NAME)
			print(Z_FILE)
			io.imsave(Z_FILE, stitched_img[z,:,:])

		print("Time to read and split image:" + str(time.time() - start_time))

	# Create spacetx format for starfish
	primary_image_dimensions: Mapping[Union[str, Axes], int] = {
		Axes.ROUND: 1, # only change this if processing rounds together, otherwise, keep at 1
		Axes.CH: CHANNEL_NUM,
		Axes.ZPLANE: Z_NUM,
	}

	start_time = time.time()
	write_experiment_json(
		path=TX_FORMATTED_DIR,
		fov_count=FOV_NUM,
		tile_format=ImageFormat.TIFF,
		primary_image_dimensions=primary_image_dimensions,
		primary_tile_fetcher=ImageTileFetcher(TX_ORIGINAL_DIR),
		aux_name_to_dimensions={},
		dimension_order=(Axes.ROUND, Axes.CH, Axes.ZPLANE)
	)

	print("Time to convert all channels to spaceTx:" + str(time.time() - start_time))
