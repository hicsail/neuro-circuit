#!/bin/bash
scc-centos7
module load anaconda3
conda create -n DLC_venv python=3.6
activate DLC_venv
pip install deeplabcut
conda install -c conda-forge wxpython 
