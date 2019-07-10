#!/bin/bash
cd ../../code/
echo "activating environment"
conda activate dlc-windowsGPU
python label.py
read -p "all set: press enter to continue"