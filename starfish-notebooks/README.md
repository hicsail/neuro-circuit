
# Getting Started
## Python
You must install Python 3.6 or higher (or use a Python 3.6 or higher environment) in order to use starfish.  You can set up a virtual environment using pyenv or conda.

For PC users, it may be easier to use Anaconda to create a virtual environment.  This will give you access to other Python APIs (such as Jupyter Notebook) which you will need to have to run the example jupyter notebooks in the starfish-notebooks folder.

You can download and install Anaconda by following the link below and selecting your operating system:
[https://www.anaconda.com/distribution/#download-section]

When Anaconda is installed, you will be able to open its GUI, Anaconda Navigator, and create a virtual environment with the right Python version from there.


## Running the Example Notebooks
Once you have installed Python (or are in your environment), install starfish using your terminal or command line:
`pip install starfish`

If you did not use Anaconda earlier and you do not have Jupyter Notebook , you will have to install it by typing this in your terminal/command line:
`pip install jupyter`

To run any of the example notebooks, navigate to the starfish-notebooks folder in your terminal or command line and type
`jupyter notebook`

From there, you can select which notebook you would like to view, and run each of the cells in that notebook.


## Data from Amazon AWS S3 Buckets
If you need to retrieve data from or put data into an AWS S3 Bucket, you will first need to install the  AWS CLI.  You can install it by following the link below, scrolling to the bottom, and selecting your operating system:
[https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html]

Once you have installed the CLI, you can use the command below in your terminal/command line to move data from your source to your destination (whether that is between buckets, from a bucket to your machine, or from your machine to a bucket):

`aws s3 cp <source_folder_name> <destination_folder_name> --no-sign-request --recursive`

Bucket names should begin with the prefix `s3://`