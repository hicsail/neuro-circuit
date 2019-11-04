
import subprocess
import argparse
import os
import re

TERA_EXE_DIR = "Z:/Personnel/Abed/Software/buildtera2/bin/Release/terastitcher.exe"

parser = argparse.ArgumentParser()
parser.add_argument("--input_folder", "-i", help="file format of the tiles")
parser.add_argument("--output_folder", "-o", help="directory of the tiles")

args = parser.parse_args()
input_folder = args.input_folder
output_folder = args.output_folder

print(input_folder)
print(output_folder)
print(os.path.abspath(input_folder))
xml_path = input_folder + '\\\\xml_merging.xml'
print(xml_path)
print(type(xml_path))

with open(xml_path,"r") as file1:
    txt=file1.read()
#    print(txt.find(os.path.abspath(input_folder)))
#    print(txt.replace(os.path.abspath(input_folder), os.path.abspath(output_folder))[:500])
    with open(output_folder + '\\\\xml_merging.xml',"w+") as file2:
        file2.write(txt.replace(os.path.abspath(input_folder), os.path.abspath(output_folder)))



def ts_merge(algorithm='SINBLEND', 
				volout_plugin="TiledXY|3Dseries",
				resolution=0,
				slicewidth=-1,
				sliceheight=-1,
				imout_depth=16,
				# R0=0, R1=2,
				# C0=0, C1=2,
				# D0=0, D1=100,
				):
	'''
	'''
	subprocess.call([TERA_EXE_DIR, '--merge', 
		['--projin=', output_folder + '\\\\xml_merging.xml'], 
		['--volout=',output_folder],
		['--algorithm=', algorithm],
		['--resolutions=', '['+str(resolution)+']'],
		['--slicewidth=', str(slicewidth)],
		['--sliceheight=', str(sliceheight)],
		['--volout_plugin=', volout_plugin],
		['--imout_depth=', str(imout_depth)],
		# ['--R0=', str(R0)],
		# ['--R1=', str(R1)],
		# ['--C0=', str(C0)],
		# ['--C1=', str(C1)],
		# ['--D0=', str(D0)],
		# ['--D1=', str(D1)],
		])


ts_merge(resolution=0)
