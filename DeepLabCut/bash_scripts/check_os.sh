#!/usr/bin/env bash
platform="$(uname -s)"
case "${platform}" in
    Linux)     
		echo "${platform} is unsupported as of right now";;
    Darwin*)    
		# Mac
		install_yaml="dlc-macOS-CPU";;
    MINGW*)     
		# Windows
		if wmic path win32_VideoController get name | grep -q "NVIDIA"; then
			install_yaml="dlc-windowsGPU"
		else
			install_yaml="dlc-windowsCPU"
		fi
		;;
    *)          
		echo "Unknown machine. Task aborted."
		exit 1
esac

echo $install_yaml