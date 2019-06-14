import subprocess
# from subprocess import Popen, PIPE

# check OS
from sys import platform
if platform == "linux" or platform == "linux2":
    print("unsupported as of right now")
elif platform == "darwin":
    print("You are using a Mac")
elif platform == "win32":
    print("You are using a Windows")
    process = subprocess.check_output("conda env create -f dlc-windowsGPU.yaml -n 6_11_5_29-dlc-windowsGPU")
    process = subprocess.check_output('conda activate 6_11_5_29-dlc-windowsGPU')