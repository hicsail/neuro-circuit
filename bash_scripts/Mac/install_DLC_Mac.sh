#!/bin/bash
echo "creating environment"
conda env create -f dlc-macOS-CPU.yaml -n test-dlc-macOS-CPU
echo "activating environment"
source activate test-dlc-macOS-CPU
# link to Jupyter Notebook just in case we run Jupyter Notebook
conda install nb_conda -y
read -p "all set: press enter to continue"