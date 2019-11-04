import subprocess
import argparse
import os
import xmltodict

class TeraStitcherWrapper():


	def __init__(self, ts_dir, input_dir, output_folder):
		
		self.ts_dir = ts_dir
		self.input_dir = input_dir
		self.output_folder = output_folder

	def ts_help(self):
		
		subprocess.call([self.ts_dir, '--help'])

	def ts_import(self, ref1=1, ref2=2, ref3=3,
					vxl1=.16, vxl2=.16, vxl3=.4,
					volin_plugin="TiledXY|3Dseries",
					):
		'''
		imports the hierarchy of folders into terastitcher
		'''
		subprocess.call([self.ts_dir, '--import', 
			['--volin=', self.input_dir], 
			['--projout=', 'xml_import'], 
			['--ref1=', str(ref1)],
			['--ref2=', str(ref2)],
			['--ref3=', str(ref3)],
			['--vxl1=', str(vxl1)],
			['--vxl2=', str(vxl2)],
			['--vxl3=', str(vxl3)],
			['--volin_plugin=', volin_plugin],
			])
		print('finished importing')

	def ts_compute_displacement(self, algorithm='MIPNCC',
								sV=25, sH=25, sD=25, 
								# R0=0, R1=2,
								# C0=0, C1=2,
								# D0=0, D1=99,
								subvoldim=100
								):
		'''
		'''
		subprocess.call([self.ts_dir, '--displcompute', 
			['--projin=', os.path.join(self.input_dir , 'xml_import.xml')], 
			['--projout=','xml_displcomp'], 
			['--subvoldim=', str(subvoldim)],
			['--algorithm=', algorithm],
			['--sV=', str(sV)],
			['--sH=', str(sH)],
			['--sD=', str(sD)],
			# ['--R0=', str(R0)],
			# ['--R1=', str(R1)],
			# ['--C0=', str(C0)],
			# ['--C1=', str(C1)],
			# ['--D0=', str(D0)],
			# ['--D1=', str(D1)],
			])

		print('displacement compute done!')
	def ts_displacement_projection(self):
		'''
		'''
		subprocess.call([self.ts_dir, '--displproj', 
			['--projin=', os.path.join(self.input_dir ,  'xml_displcomp.xml')], 
			['--projout=','xml_displproj'], 
			])

	def ts_displacement_threshold(self, threshold=.7):
		'''
		'''
		subprocess.call([self.ts_dir, '--displthres', 
			['--projin=', os.path.join(self.input_dir , 'xml_displproj.xml')], 
			['--projout=','xml_displthres'], 
			['--threshold=', str(threshold)],
			])

	def ts_displacement_tiles(self):
		'''
		'''
		subprocess.call([self.ts_dir, '--placetiles', 
			['--projin=', os.path.join(self.input_dir , 'xml_displthres.xml')], 
			['--projout=','xml_merging'], 
			])

	def ts_merge(self, algorithm='SINBLEND', 
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
		subprocess.call([self.ts_dir, '--merge', 
			['--projin=', os.path.join(self.input_dir , 'xml_merging.xml')], 
			['--volout=',self.output_folder],
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


if __name__ == "__main__":

	ts_dir = "Z:/Personnel/Abed/Software/buildtera2/bin/Release/terastitcher.exe"
	# input_dir = r"X:\ARG_Analysis\Round04\Sample2\561\sample2round43x3multipoint_XX_561"
	# output_dir = r"X:\ARG_Analysis\Round04\Sample2\561\sample2round43x3multipoint_XX_561"


	# initiate the parser
	parser = argparse.ArgumentParser()

	parser.add_argument("--ts_dir", "-t", help="file format of the tiles",
							default=ts_dir)
	parser.add_argument("--input_dir", "-i", help="file format of the tiles")
	parser.add_argument("--output_dir", "-o", help="folder address with no \ at the end")

	# read arguments from the command line
	args = parser.parse_args()
	ts_dir = args.ts_dir
	input_dir = args.input_dir
	output_dir = args.output_dir

	with open(input_dir + '/xml_import.xml') as fd:
	    doc = xmltodict.parse(fd.read())
	znum = int(doc['TeraStitcher']['dimensions']['@stack_slices'])

	print('Z dimension: ' + (str(znum)) )

	obj = TeraStitcherWrapper(ts_dir, input_dir, output_dir)
	obj.ts_import()
	obj.ts_compute_displacement(sV=25, sH=25, sD=1, subvoldim = znum-1)
	obj.ts_displacement_projection()
	obj.ts_displacement_threshold(threshold=.7)
	obj.ts_displacement_tiles()
	obj.ts_merge(resolution=0)
