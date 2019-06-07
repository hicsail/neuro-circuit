# neuro-circuit

## Must-Know-Knowledge

* It is highly recommended for you to read the user_guide here: <https://github.com/hicsail/neuro-circuit//blob/master/DLC_user_guide.pdf>
* We assume you have installed conda. Instructions here: <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>

How to write files with the "sh" extension?

1. Step one:

   - Windows: 

     Open the command prompt as an administrator (**must run as administration**)

     Hints here: <https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>

   - Mac:

     Open terminal

     Hints here: https://macpaw.com/how-to/use-terminal-on-mac

2. Step two: 

   enter "cd <path>" where <path> is your system path to the shell script

   Example: "cd C:\Users\Zack\Documents\GitHub\neuro-circuit\whiskers" if I have a script in the folder whiskers

3. Step three:

   - Windows: 

     In command prompt, enter "<name_of_script>" and press enter

     Example: "script.sh"

   - Mac:

     In terminal, enter "sh <name_of_script>" and press enter

     Example: "sh script.sh"

4. Step four:

   When the script is finished, it generally should output "all set: press enter to continue."

   If there is no error among the previous output, just press any key in its window to exit the script. Otherwise, feel free to consult <https://github.com/AlexEMG/DeepLabCut/wiki/Troubleshooting-Tips> or contact us (see below).

   Additionally, if something goes wrong with the software, feel free to check the errors displayed in that window.

# Workflow

## 1. Installing DeepLabCut (& Create the Conda Environment)

In the folder bash_scripts, run the file whose name ends with "sh" and having the same system as yours (Win/Mac)

## 2. Create Project

1. Enter the folder whiskers

2. Put target videos in the "raw_videos" folder

3. Windows: run "Win_create_project.sh"

   Mac: run "Mac_create_project.sh.sh"

4. Open the "config.yaml" file with the notebook app, and change the categories under "body_parts."

   For other parameters, please refer to the user guide. A basic understanding of YAML files is helpful (this is more than enough: <https://learnxinyminutes.com/docs/yaml/>)

## 2. Extract Frames (for Labeling)

1. Run the script named "extract_frames.sh" that matches your system

2. In the prompt window, you need to enter "yes" and press the enter key for the new videos you want to extract frames. For old videos, press "no"

## 3. Label

1. Inside the folder whiskers

2. Run the script named "label_frames_DLC" that matches your system

3. You would encounter an interface for labeling. Click "Load frames" and select the folder you want to label in "...(path to the whiskers folder)...\whiskers\whiskers-sail-2019-06-07\labeled-data"

   **Note the folder is misleading since it contains both labeled and unlabeled images.*

4. Click "help" for help.

   *Click "Save" often and before quitting to save the work.

   *Feel free to quit if you decide to take a break. Just launch it again and your work would be there.

## *To Add New Videos (In any State)* 

1. Put new videos in the "raw_videos" folder
2. Perform extraction, labeling as needed

## Ask Questions

Contact BU SAIL

shreyap@bu.edu

zackL@bu.edu