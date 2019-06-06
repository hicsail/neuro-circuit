#!/usr/bin/env python
# coding: utf-8

# # DeepLabCut Toolbox - DEMO (mouse reaching)
# https://github.com/AlexEMG/DeepLabCut
# 
# Nath\*, Mathis\* et al. *Using DeepLabCut for markerless pose estimation during behavior across species
# user guide: https://www.biorxiv.org/content/10.1101/476531v1
# 
# This notebook demonstrates the use of the DeepLabCut toolbox for a provided demo dataset based on *Somatosensory Cortex Plays an Essential Role in Forelimb Motor Adaptation in Mice* by Mathis et al., Neuron 2017. DOI:https://doi.org/10.1016/j.neuron.2017.02.049
# 
# This notebook illustrates how to:
# - plot the labeled images
# - train a network
# - evaluate a network
# - analyze a novel video
# - create an automatically labeled video 
# - plot the trajectories 
# - identify outlier frames
# - annotate the outlier frames manually
# - merge the data sets and update the training set
# - train a network
# 
# Note: This notebook starts from an already initialized project with labeled data.

#  Note: The noteboks will not work in Docker, as Docker is designed to not display GUIs. Please follow the steps outlined here: https://github.com/AlexEMG/DeepLabCutbeta/blob/master/docs/UseOverviewGuide.md#option-2-using-terminal-start-python

# # Not in Colab or Docker, great, then start here!
# 
# First, be sure you are in the Anaconda Python! Go to "Kernel > Change Kernel > and selection Python [conda enc: DLC2]" (or whatever you call your conda environment!

# ## Import the DLC toolbox:

# In[1]:


from IPython import get_ipython

import os
os.environ['FOR_DISABLE_CONSOLE_CTRL_HANDLER'] = '1'
# get_ipython().magic('matplotlib inline')

import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))


# In[2]:


import deeplabcut


# In[3]:


# OPTIONAL: just an example of how for you to see that TF is here!
import tensorflow as tf
tf.__version__


# When you use DeepLabCut on your own data, you will (1) create a project, (2) extract frames to label, and (3) label you data. In this demo, this is all done for you. The purpose of the demo to for you to get familiar with the workflow (and check your installation).

# In[4]:


# Loading example data set, st config_path and creating the training set: 
import os
# Note that parameters of this project can be seen at: *Reaching-Mackenzie-2018-08-30/config.yaml*
from pathlib import Path

#create a variable to set the config.yaml file path:
path_config_file = os.path.join(os.getcwd(),'Reaching-Mackenzie-2018-08-30/config.yaml')

#let's load some demo data, and create a training set (this function is not used when you create your own project):
deeplabcut.load_demo_data(path_config_file)


# In[5]:


#Perhaps plot the labels to see how the frames were annotated:
deeplabcut.check_labels(path_config_file)


# *Note: in this demo the training set was already created, so you don't need to do this and can directly proceed to train the network!*

# ## Start training of Feature Detectors
# This function trains the network for a specific shuffle of the training dataset. **The user can set various parameters in /Reaching-Mackenzie-2018-08-30/dlc-models/ReachingAug30-trainset95shuffle1/iteration-0/train/pose_cfg.yaml.**
# 
# Training can be stopped at any time. Note that the weights are only stored every 'save_iters' steps. For this demo the it is advisable to store & display the progress very often (i.e. display every 20, save every 100). In practice this is inefficient.  **Go change the pose_cfg file now!**
# 
# **We recommend just training for 10-20 min, as you aren't running this demo to use DLC, just to work through the steps. In total, this demo should take you LESS THAN 1 HOUR!**

# In[ ]:


deeplabcut.train_network(path_config_file, shuffle=1, saveiters=300, displayiters=10)
#notice the variables "saveiters" and "dsiplayiters" that can be set in the function

#you just need to run this until you get at least 1 snapshot, which is set by: "save_iters" 
#(so in this case you could stop after 500!) How do I stop? Click the STOP button!
# To train until ~300 iterations on a CPU should be ~6 min


# *Note, that if it reaches the end (defualt 1M) or you stop it (by "stop" or by CTRL+C), 
# you will see an "error", but it is not a real error, i.e. you can ignore this.*

# ## Evaluate the trained network
# 
# This function evaluates a trained model for a specific shuffle/shuffles at a particular training state (snapshot) or on all the states. The network is evaluated on the data set (images) and stores the results as .csv file in a subdirectory under **evaluation-results**.
# 
# You can change various parameters in the ```config.yaml``` file of this project. For the evaluation one can change pcutoff. This cutoff also influences how likely estimated postions need to be so that they are shown in the plots.

# In[ ]:


deeplabcut.evaluate_network(path_config_file,plotting=True)


# **NOTE: depending on your set up sometimes you get some "matplotlib errors, but these are not important**
# 
# Now you can go check out the images. Given the limted data input and it took ~20 mins to test this out, it is not meant to track well, so don't be alarmed. This is just to get you familiar with the workflow... 

# ## Analyzing videos
# This function extracts the pose based on a trained network from videos. The user can choose the trained network - by default the most recent snapshot is used to analyse the videos. However, the user can also specify the snapshot index for the variable **snapshotindex** in the **config.yaml** file).
# 
# The results are stored in hd5 file in the same directory, where the video resides. The pose array (pose vs. frame index) can also be exported as csv file (set flag to...). 

# In[ ]:


# Creating video path:
# You'll need to edit this for your folder! 

#The video can be the one you trained with and new videos that look similar, i.e. same experiments, etc.
# You can add individual videos, OR just a folder - it will skip videos that are already analyzed once.

videofile_path = ['/home/mackenzie/DEEPLABCUT/DeepLabCut2.0/examples/Reaching-Mackenzie-2018-08-30/videos/MovieS2_Perturbation_noLaser_compressed.avi']                           


# In[ ]:


print("Start Analyzing the video!")
deeplabcut.analyze_videos(path_config_file,videofile_path)
# this video takes ~ 8 min to analyze with a CPU


# *NOTE: Yes, this is slow on a CPU (a GPU is MUCH faster)... see https://www.biorxiv.org/content/early/2018/10/30/457242 if you are interested!*

# ## Create labeled video
# 
# This function is for the visualization purpose and can be used to create a video in .mp4 format with the predicted labels. This video is saved in the same directory, where the (unlabeled) video resides. 
# 
# Various parameters can be set with regard to the colormap and the dotsize. The parameters of the 

# In[ ]:


deeplabcut.create_labeled_video(path_config_file,videofile_path)


# ## Plot the trajectories of the analyzed videos
# This function plots the trajectories of all the body parts across the entire video. Each body part is identified by a unique color. The underlying functions can easily be customized.

# In[ ]:


get_ipython().magic('matplotlib notebook')
deeplabcut.plot_trajectories(path_config_file,videofile_path,showfigures=True)

#These plots can are interactive and can be customized (see https://matplotlib.org/)


# ## Extract outlier frames, where the predictions are off.
# 
# This is optional step allows to add more training data when the evaluation results are poor. In such a case, the user can use the following function to extract frames where the labels are incorrectly predicted. Make sure to provide the correct value of the "iterations" as it will be used to create the unique directory where the extracted frames will be saved.

# In[ ]:


deeplabcut.extract_outlier_frames(path_config_file,videofile_path,outlieralgorithm='uncertain',p_bound=.2)


# In[ ]:


# Note, if you have questions on parameters, remember "?" gives you answers:
# i.e. deeplabcut.extract_outlier_frames?


# The user can run this iteratively, and (even) extract additional frames from the same video.

# ## Manually correct labels
# 
# This step allows the user to correct the labels in the extracted frames. Navigate to the folder corresponding to the video 'MovieS2_Perturbation_noLaser_compressed' and use the GUI as described in the protocol to update the labels.

# In[ ]:


#GUI pops up! 

get_ipython().magic('gui wx')
deeplabcut.refine_labels(path_config_file)


# In[ ]:


# Now merge datasets (once you refined all frames)
deeplabcut.merge_datasets(path_config_file)


# ## Create a new iteration of training dataset, check it and train...
# 
# Following the refine labels, append these frames to the original dataset to create a new iteration of training dataset.

# In[ ]:


#Perhaps plot the labels to see how how all the frames are annoted (including the refined ones)
deeplabcut.check_labels(path_config_file)


# In[ ]:


deeplabcut.create_training_dataset(path_config_file)


# Now one can train the network again... (with the expanded data set)

# In[ ]:


deeplabcut.train_network(path_config_file)

