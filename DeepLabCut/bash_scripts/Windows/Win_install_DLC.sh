#!/bin/bash
echo "creating environment"
conda create -f dlc-windowsGPU.yaml -n dlc-windowsGPU
echo "activating environment"
activate dlc-windowsGPU
# link to Jupyter Notebook just in case we run Jupyter Notebook
conda install nb_conda -y
read -p "all set: press enter to continue"