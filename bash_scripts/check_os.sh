#!/usr/bin/env bash
platform="$(uname -s)"
case "${platform}" in
    Linux)     
		echo "${machine} is unsupported as of right now";;
    Darwin*)    
		machine="Mac"
		install_yaml="dlc-macOS-CPU";;
    MINGW*)     
		machine="Windows"
		install_yaml="dlc-windowsGPU";;
    *)          
		machine="UNKNOWN:${platform}"
		echo "Unknown machine. Task aborted."
		exit 1
esac

echo $install_yaml