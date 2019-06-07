#!/bin/bash
echo "creating environment"
conda env create -f dlc-windowsGPU.yaml -n dlc-windowsGPU
# link to Jupyter Notebook just in case we run Jupyter Notebook
conda install nb_conda -y
echo "activating environment"
activate dlc-windowsGPU
read -p "all set: press enter to continue"