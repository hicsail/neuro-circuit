#!/bin/bash
echo "activating environment"
conda activate dlc-windowsGPU
python run.py
read -p "all set: press enter to continue"