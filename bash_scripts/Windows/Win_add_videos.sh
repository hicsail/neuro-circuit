#!/bin/bash
cd ../../whiskers/
echo "activating environment"
conda activate dlc-windowsGPU
python add_videos.py
read -p "all set: press enter to continue"