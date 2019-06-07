#!/bin/bash
# move to /c/Users/YOUR_USERNAME/Documents/GitHub/neuro-circuit/bash_scripts
echo "activating environment"
source activate test-dlc-macOS-CPU
python run.py
read -p "all set: press enter to continue"