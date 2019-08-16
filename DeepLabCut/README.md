# Using DeepLabCut

## Necessary-Prior-Knowledge

1. It is highly recommended for you to read the [user guide](<https://github.com/hicsail/neuro-circuit//blob/master/DLC_user_guide.pdf>)
2. A basic understanding of YAML files is helpful ([this is more than enough](<https://rollout.io/blog/yaml-tutorial-everything-you-need-get-started/>))


## Workflow

### 1. Installation

1. Make sure to have Conda. You can install it [here](<https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>)

2. If using Windows

   * make sure to have *Git Bash*. You can install it [here](https://gitforwindows.org/)

   * have an NVIDIA driver installed, and CUDA (currently, TensorFlow 1.13 is installed inside the env, so you can install CUDA 10 and an appropriate driver)

     DRIVERS: https://www.nvidia.com/Download/index.aspx

     CUDA: https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#verify-you-have-cuda-enabled-system
     
     [Versions to Use/Troubleshooting](https://github.com/AlexEMG/DeepLabCut/blob/master/docs/installation.md#troubleshooting)

### 2. Environment & Project Creation

Tips

* When you have accidentally made a mistake, if you have not put too much work in, it is often best to 

  * delete the project folder 

  * or even the conda environment (as well as the environment folder usually located at C:\Users\<Username>\\.conda\envs) 

  and start the script over

* If something goes wrong with the software, feel free to check the errors displayed in that window

* If there is no error among the previous output, just press any key in its window to exit the script. Otherwise, feel free to consult [the original repository's troubleshooting tips](<https://github.com/AlexEMG/DeepLabCut/wiki/Troubleshooting-Tips>) or contact us (see button).

Instructions

1. Open the "pre_config.yaml" file with a text editor, and change the parameters to suit your project (see explanations of most of the parameters in the guide mentioned in "necessary-prior-knowledge")

2. Run "initial_setup.sh" in the folder "bash_scripts" (instructions below)

   **Do not exit even if the terminal shows "Done" as there are more steps.** It typically takes 10-15 minutes the first time.

   You are recommended to run files with the "sh" extension in the following manner

   * Step one
  * Windows: 
   
    Run Git Bash (**must run as administration**)
   
    [Optional: always make an app run in admin](https://www.groovypost.com/howto/make-windows-10-apps-always-run-with-administrator-privileges/)

   **Note: if you don't have "(base)" in the front of the prompt, and you get an error when running "conda activate base", there is probably some problem with your Git Gash and Conda**

   A workaround is to 

   1. run windows command prompt
   2. run the command: activate  <Conda path in quotes> such as "C:\Users\sail\Anaconda3_1"
   3. go to the directory of the script
   4. run the script with just the name of the script

  * Mac:
   
    Run Terminal ([Hints here](https://macpaw.com/how-to/use-terminal-on-mac))


   * Step two

     Enter "cd <path>" where <path> is your system path to the shell script

     Example: "cd C:\Users\Zack\Documents\GitHub\neuro-circuit\DeepLabCut\bash_scripts" if I have a script in the folder bash_scripts

   * Step three

     - Windows: 

       In command prompt, enter "<name_of_script>" and press enter

       Example: "script.sh"

     - Mac:

       In terminal, enter "sh <name_of_script>" and press enter

       Example: "sh script.sh"

   * Step four

     When the script is finished, it generally should output "all set: press enter to continue."

3. If you have selected manual frame-extraction, the extracting GUI would launch

   *Note you may get an error by selecting Load Videos but closing the file explorer without choosing anything*

4. The labeling GUI would launch

   * Click "Load frames"

   * Each video would have its own folder (named same as the video) in ".../<working_directory> aka the project folder\labeled-data\" (which needs to be a full path)

   * Select the folder for the video you want to label

     *Note the folder name is misleading since it contains both labeled and unlabeled images*

   Feel free to quit if you decide to take a break. Continue labeling by the step below: "Continue to Label"

### 3. Continuous Labeling

Run "label_frames.sh" in the folder "bash_scripts"

# Additional Notes for [The Chen Lab ](https://sites.bu.edu/chenlab/) at BU

### 1. Handle videos on the SCC

* At the BUSCC, you can access the network drive by

  "sg <groupname>" where <groupname> is the name of the group/organization registered on the SCC

  "mount -t cifs -o username=<username> \\<address>\data /media/data", assuming you want to access the data folder

* Some helpful scripts are at "code\select_training_videos_SCC"

### 2. Refer to file locations on the Network Drive

If you want to refer to the path "Z:/data/raw_videos/" assuming the network drive is "Z:",

you should do \\\\128.197.168.188\data1 assuming 128.197.168.188 is its address (Z needs not to be there)

## Questions?

Contact BU SAIL

hicsail@bu.edu