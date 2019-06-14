#!/usr/bin/env bash
# System
install_yaml=$(check_os.sh)
source activate $install_yaml
cd ../whiskers/
python label.py
read -p "all set: press enter to continue"