#!/bin/bash
echo "creating environment"
conda env create -f dlc-windowsGPU.yaml -n test-dlc-windowsGPU
# link to Jupyter Notebook just in case we run Jupyter Notebook
conda install nb_conda
echo "activating environment"
activate test-dlc-windowsGPU
pip install deeplabcut
pip install tensorflow
conda install python.app
