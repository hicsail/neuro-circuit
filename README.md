# neuro-circuit

## Necessary-Prior-Knowledge

1. It is highly recommended for you to read the user guide here: <https://github.com/hicsail/neuro-circuit//blob/master/DLC_user_guide.pdf>
2. A basic understanding of YAML files is helpful (this is more than enough: <https://rollout.io/blog/yaml-tutorial-everything-you-need-get-started/>)

3. How to run files with the "sh" extension?
   1. Step one:

      - Windows: 

        Open the command prompt as an administrator (**must run as administration**)

        Hints here: <https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>

      - Mac:

        Open terminal

        Hints here: https://macpaw.com/how-to/use-terminal-on-mac

   2. Step two: 

      Enter "cd <path>" where <path> is your system path to the shell script

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

      * If there is no error among the previous output, just press any key in its window to exit the script. Otherwise, feel free to consult <https://github.com/AlexEMG/DeepLabCut/wiki/Troubleshooting-Tips> or contact us (see below).

      * Additionally, if something goes wrong with the software, feel free to check the errors displayed in that window

   # Workflow

## 1. Installing DeepLabCut (& Create the Conda Environment)

0. We assume you have installed Conda. If not, instructions are here: <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>

1. Open the "pre_config.yaml" file in the folder "whiskers" with the notebook app, and change the parameters to suit your project

2. (If using Windows, **run the following file as administrator**

   Hints here: <https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>) 

3. Run "initial_setup.sh" in the folder "bash_scripts"

4. If you have selected for manual frame-extraction, the GUI would launch.

5. The labeling GUI would launch.

   * You would encounter an interface for labeling. Click "Load frames" and select the folder you want to label in "...(path to the whiskers folder)...\whiskers\whiskers-sail-2019-06-07\labeled-data"

   **Note the folder is misleading since it contains both labeled and unlabeled images.*

   * Click "help" for help.

   * Click "Save" often and before quitting to save the work.

   * Feel free to quit if you decide to take a break. Just launch it again and your work would be there.

## 2. Continue to Label

Run "label_frames.sh" in the folder "bash_scripts"

## Questions?

Contact BU SAIL

shreyap@bu.edu

zackL@bu.edu