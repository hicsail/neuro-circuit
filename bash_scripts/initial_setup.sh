#!/usr/bin/env bash
echo "Checking Conda updates"
conda update -y -n base -c defaults conda
# System
echo "Checking system"
platform="$(uname -s)"
# platform="safsf"
case "${platform}" in
    Linux)     
		echo "${machine} is unsupported as of right now";;
    Darwin*)    
		machine="Mac"
		install_yaml="dlc-macOS-CPU";;
    MINGW*)     
		machine="Windows"
		install_yaml="dlc-windowsGPU";;
    *)          
		machine="UNKNOWN:${platform}"
		echo "Unknown machine. Task aborted."
#		exit 1
esac

## Environment
echo "Creating environment from $install_yaml.yaml"
conda env create -f $install_yaml.yaml
#conda create -f $install_yaml
echo "Activating the new environment"
source activate $install_yaml
# link to Jupyter Notebook just in case we run Jupyter Notebook
conda install nb_conda -y

# Project
cd ../whiskers/
python create_project_and_extract_frames.py
python label.py
# Finished
read -p "all set: press enter to continue"