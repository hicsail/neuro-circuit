#!/usr/bin/env bash
echo "Checking Conda updates"
conda update -y -n base -c defaults conda

# System
chmod +x ./check_os.sh
install_yaml=$(./check_os.sh)
## Environment
echo "Creating environment from $install_yaml.yaml"
conda env create -f $install_yaml.yaml

echo "Activating the new environment"
source activate $install_yaml

# link to Jupyter Notebook just in case we run Jupyter Notebook
conda install nb_conda -y

# Project
cd ../code/
python create_project.py
python extract.py
python label.py
cd ../bash_scripts/
# Finished
read -p "all set: press enter to continue"
