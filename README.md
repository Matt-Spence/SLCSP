# SLCSP

This project contains code solving the Ad Hoc homework challence SLCSP. In this challenge, we are asked to find the Second Lowest Cost Silver Plan for a given US zip code. All files necessary to run and test this project are located within this repository. 

## How To Run the Project
To run this project, first make sure python3 is installed on your system. You can check this by running ```python3 --version``` in your terminal/command prompt. If the command fails, instructions to install python3 can be found [here](https://www.python.org/downloads/). 

Next, make sure that the python3 package manager pip3 is installed on your system. You can check this by running ```pip3 -v``` in your terminal/command prompt. Instructions for installation can be found [here](https://www.geeksforgeeks.org/how-to-install-pip-in-linux/).

You will need to install the python library ```pandas``` to run this project. This can be accomplished by running ```pip3 install pandas``` in your terminal/command prompt.

Once all this is done, you can run the project! Navigate the the main /SLCSP directory and run the following command: ```python3 slcsp.py```

To run the provided tests, run the following command from the main /SLCSP directory: ```python3 -m unittest test_slcsp.py```

## Development Environment
This repo was written using VSCode on PopOS 22.04 LTS, which is an Ubuntu-based Linux distribution. However, this code should run just fine on any system which can install a python3 interpreter (AKA pretty much all of them). 