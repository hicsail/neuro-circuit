#!/bin/bash
cd ../../whiskers/
echo "activating environment"
conda activate dlc-windowsGPU
python create_project.py
read -p "all set: press enter to continue"