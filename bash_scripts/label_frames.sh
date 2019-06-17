#!/usr/bin/env bash
# System
install_yaml=$(./check_os.sh)
source activate $install_yaml
cd ../whiskers/
if [ "$install_yaml" == "dlc-macOS-CPU" ]
	pythonw label.py
then
	python label.py
fi
read -p "all set: press enter to continue"
