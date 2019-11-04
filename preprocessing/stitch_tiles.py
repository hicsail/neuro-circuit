import argparse
import os
from shutil import copyfile, rmtree
from terastitcher_wrapper import TeraStitcherWrapper
import xmltodict
import glob

TERA_FOLDER = 'tera_tiles'
STITCHED_FOLDER = '02_Stitched'
TERA_EXE_DIR = "Z:/Personnel/Abed/Software/buildtera2/bin/Release/terastitcher.exe"


if __name__ == "__main__":
	# parse inputs
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_file", "-f", help="file format of the tiles")
	parser.add_argument("--input_dir", "-d", help="directory of the tiles")
	parser.add_argument("--grid_size", "-g", help="2 digit number representing grid dimension. e.g. 43 --> 4x3 grid")
	parser.add_argument("--spacing", "-s", help="assuming equal space in x/y directions, how much we move between tiles")


	args = parser.parse_args()
	file_format = args.input_file
	input_dir = args.input_dir
	spacing = int(args.spacing)
	grid_size = args.grid_size

	os.chdir(input_dir)
	filenames = [file for file in glob.glob("*.tif")]
	alphabet = list('ABCDEFGHIJK')
	tilenames = []
	for filename in filenames:
	    for i in range(len(alphabet)):
	        for j in range(10):
	            if filename.find('_'+alphabet[i]+str(j+1)) != -1:
	                tilenames.append(alphabet[i]+str(j+1).upper())

	grid_size = [int(args.grid_size[0]), int(args.grid_size[1])] 

	assert grid_size[0]*grid_size[1] == len(tilenames),  "tilenames and grid_size don't match"

	coordinates = [str(i*spacing*10).zfill(6) for i in range(max(grid_size))]

	#check that we have access to Z drive
	if not os.path.exists(TERA_EXE_DIR):
		raise FileNotFoundError('Cannot find TeraStitcher. Is the Z drive accessible?')

	#check that input directory exists
	assert os.path.isdir(input_dir), "input directory doesn't exist!"

	#check that file format is correct
	if file_format.find('##') == -1:
		raise SyntaxError('You must replace the coordinate with ##')

	# create directories
	filelist=[]
	for tile_coord in tilenames:
		filename = file_format.replace('##', tile_coord)
		if not os.path.exists(os.path.abspath(os.path.join(input_dir, filename))):
			raise FileNotFoundError(filename + ' does not exist. Are you sure it is spelled correctly?')
		filelist.append(filename)

	skip = False
	tera_dir = os.path.abspath(os.path.join(input_dir, TERA_FOLDER))
	if os.path.exists(tera_dir):
		folder_check = input("folder already exists, overwrite? [y/n]")
		if folder_check == 'y':
			rmtree(tera_dir, ignore_errors=True)
			os.makedirs(tera_dir)
		else:
			skip = True
	else:
		os.makedirs(tera_dir)

	if not skip:
		for i in range(grid_size[0]): # row
		    os.mkdir(tera_dir+'\\'+coordinates[i])
		    for j in range(grid_size[1]): # col
		        dst_tile = tera_dir+'\\'+coordinates[i]+'\\'+coordinates[i]+'_'+coordinates[j]+'\\'
		        os.mkdir(dst_tile)
		        copyfile(input_dir + '\\' + filelist[j+i*grid_size[1]], dst_tile + '\\' +coordinates[0]+'.tif')
		        print( filelist[j+i*grid_size[1]] + ' ---> ' + dst_tile)

	stitch_check = input("do you want to stitch? [y/n]")
	if stitch_check == 'y':

		# check that output directory exists
		stitched_dir = os.path.abspath(os.path.join(os.path.dirname(input_dir), STITCHED_FOLDER))
		if not os.path.isdir(stitched_dir):
			raise FileNotFoundError('You must have a 02_Stitched folder')

		# Stitch tiles
		obj = TeraStitcherWrapper(TERA_EXE_DIR, tera_dir, stitched_dir)
		obj.ts_import()

		with open(os.path.join(tera_dir , 'xml_import.xml')) as fd:
		    doc = xmltodict.parse(fd.read())
		znum = int(doc['TeraStitcher']['dimensions']['@stack_slices'])

		obj.ts_compute_displacement(sV=25, sH=25, sD=1, subvoldim = znum-1)
		obj.ts_displacement_projection()
		obj.ts_displacement_threshold(threshold=.7)
		obj.ts_displacement_tiles()
		obj.ts_merge(resolution=0)
