## Image Processing Instructions
Output of the microscope is a single ND2. This document outlines protocols and scripts involved to stitch and segment images for the Starfish pipeline. Alignment and registration will be done in Neurotator and is not discussed here.

### Folder structure
See `X:\ARG_Analysis` for example
* Round
  * Sample
    * Channel  
    ![folder-struct](images/folder-struct.png)

### Tools
* NIS Element
* [TeraStitcher](https://github.com/abria/TeraStitcher)
* [Baxter Algorithm](https://github.com/klasma/BaxterAlgorithms)

### Steps
#### 1) Convert ND2 file to 9 (3x3) TIFF tiles (NIS Element)
* Open ND2 file
* Save/export to TIFF
* Double check parameters
   * Multi-channel    
![nis-params](images/nis-multi-channel-params.png)

   * Single-channel - check "Keep Original Channel Combination"
![nis-params](images/nis-single-channel-params.png)

* Export to `01_Tiles` folder for each channel

#### 2) Stitch TIFF tiles

* Folder addresses shouldn't have space in them *

The `stitch_tiles.py` script in this directory will create the expected file hierarchy for TeraStitcher and then stitch the tiles while removing the overlap (we assume 5%).  This must be done in a separate command prompt for *every* channel.

**Tile coordinates in the file names must represent rows with letters and columns with numbers (e.g. A1-3, B1-3, C1-3)**

```
python stitch_tiles.py --input_file= --input_dir= --grid_size= --spacing=
```
- Replace tile coordinate in the file name (e.g. A1) with ##   
- Grid size is 2 digit number representing grid -dimension. e.g. 43 --> 4x3 grid   
- Spacing is the change in X/Y direction, in microns   


Example:
```
python Z:\Personnel\Abed\GitHub\neuro-circuit\preprocessing\stitch_tiles.py --input_file="slice 1 multipoint 1 (488 561)_##v2_CJC488.tif" --input_dir="Y:\Projects\CRACK\Animals\cc034\FISH\tif_exports\round4\slice1\488" --grid_size=43 --spacing=315
```
Script will take approximately ~15min to run, depending on the size of the images. Double check with ImageJ when the script is finished to make sure that the stitched image looks reasonable.

#### 3b) Downsample
Channel 561 images need to be downscaled for Baxter (16x) and for Neurotator (4x)

Place all the stacks to be downsampled into the script to be done in parallel

```
python Z:\Personnel\Abed\GitHub\tiff_resize\tif_rescale.py --file=<> --scale=4
```

Save to -> `\Stiched\4xDS\`


#### 4) Cell segmentation (Baxter Algorithm)
This step is only done on the 561 channel.
`Z:\Dropbox\Dropbox\Chen Lab Team Folder\Projects\Starotator\MINS alternatives\BaxterAlgorithms-master`


* Type `BaxterAlgorithms` in the Matlab console
* Open Experiment -> 02_Stitched folder -> Make sure it loads the 16x image
* Settings -> Settings
   * Change numZ to the number of Z slices specific to your image
   * Set zStacked to 1
   * Set bits to 12
* Save
* Settings-> Set segmentation parameters
* Start with the parameters shown below, adjust if necessary    
![baxter-params](images/baxter-params.png)

-#### 5) Space-Tx Conversion
Separate each stitched image by Z slice then combine the channels to create a Starfish compatible input. This needs to be done *per sample*.  

**The stitched image must be in the `02_Stitched` subfolder in each channel directory, and the name must be in the format `RrrSs_ccc.tif` where rr is the round number, s is the sample number, and ccc is the channel name (e.g. R05S2_561)**

`python make_spacetx.py --input_dir='' --round=# --sample=#`

Example:
```
python make_spacetx.py --input_dir='X:\ARG_Analysis\Round11\Sample2' -r=11 -s=2
```

Script will take ~2 hour to run. Output will be in `SpaceTxFormat\` with 2 subfolders:    
- `original` - TIFF files per Z slice for every channel    
- `formatted` - SpaceTx formatted TIFF files