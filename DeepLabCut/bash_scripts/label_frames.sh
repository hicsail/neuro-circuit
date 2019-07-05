#!/usr/bin/env bash
# System
install_yaml=$(./check_os.sh)
source activate $install_yaml
cd ../code/

if [ "$install_yaml" = "dlc-macOS-CPU" ]
then
	pythonw label.py
else
	python label.py
fi

cd ../bash_scripts/
read -p "all set: press enter to continue"
