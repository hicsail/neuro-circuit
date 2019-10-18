import argparse
import os
from shutil import copyfile
from terastitcher_wrapper import TeraStitcherWrapper

TILE_NAMES = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
COORDINATES = ['000010', '003150', '006300']
TERA_FOLDER = 'tera_tiles'
STITCHED_FOLDER = '02_Stitched'
TERA_EXE_DIR = "Z:/Personnel/Abed/Software/buildtera2/bin/Release/terastitcher.exe"


if __name__ == "__main__":
	# parse inputs
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_file", "-f", help="file format of the tiles")
	parser.add_argument("--input_dir", "-d", help="directory of the tiles")

	args = parser.parse_args()
	file_format = args.input_file
	input_dir = args.input_dir

	#check that we have access to Z drive
	if not os.path.exists(TERA_EXE_DIR):
		raise FileNotFoundError('Cannot find TeraStitcher. Is the Z drive accessible?')

	#check that input directory exists
	assert os.path.isdir(input_dir)

	#check that file format is correct
	if file_format.find('##') == -1:
		raise SyntaxError('You must replace the coordinate with ##')

	# check that output directory exists
	stitched_dir = os.path.abspath(os.path.join(os.path.dirname(input_dir), STITCHED_FOLDER))
	if not os.path.isdir(stitched_dir):
		raise FileNotFoundError('You must have a 02_Stitched folder')

	# create directories
	filelist=[]
	for tile_coord in TILE_NAMES:
		filename = file_format.replace('##', tile_coord)
		if not os.path.exists(os.path.abspath(os.path.join(input_dir, filename))):
			raise FileNotFoundError(filename + ' does not exist. Are you sure it is spelled correctly?')
		filelist.append(filename)

	tera_dir = os.path.abspath(os.path.join(input_dir, TERA_FOLDER))
	os.makedirs(tera_dir)
	assert os.path.exists(tera_dir)

	for i in range(3): # row
	    os.mkdir(tera_dir+'\\'+COORDINATES[i])
	    for j in range(3): # col
	        dst_tile = tera_dir+'\\'+COORDINATES[i]+'\\'+COORDINATES[i]+'_'+COORDINATES[j]+'\\'
	        os.mkdir(dst_tile)
	        copyfile(input_dir + '\\' + filelist[j+i*3], dst_tile + '\\' +COORDINATES[0]+'.tif')
	        print( filelist[j+i*3] + ' ---> ' + dst_tile)


	# Stitch tiles
	obj = TeraStitcherWrapper(TERA_EXE_DIR, tera_dir, stitched_dir)
	obj.ts_import()
	obj.ts_compute_displacement(sV=25, sH=25, sD=25)
	obj.ts_displacement_projection()
	obj.ts_displacement_threshold(threshold=.7)
	obj.ts_displacement_tiles()
	obj.ts_merge(resolution=0)
