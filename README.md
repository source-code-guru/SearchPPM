# SearchPPM

A python script which extracts the mass intentisites of a user-defined mass list from DataAnalysis proteomics software output csv files

## Features

- Parses the DataAnalysis csv files output whose file path is given in the variable "folder" (e.g. folder = "C:\\Documents\\Test\\")
- Define the mass list by straight modification of the mass_values variable (e.g. mass_values=\[589.95134, 658.87134, 798.78351, 855.55214, 989.15358\])
- Set the tolerance between the theoretical mass and the experimental mass in ppm with the variable "ppm" (e.g. ppm=4 )
- Outputs a file whose name is defined by the variable "output_file", in the current working directory, with the corresponding masses and intensities (e.g. output_file="output.csv")
  
## Requirements

- Install requirements: Python 3.10+ / Pandas / Bash + coreutils

## Installation

-Option 1:

Install Python 3.10+ from the official Python distribution for your OS.  
Upgrade pip and install pandas:

python -m pip install --upgrade pip  
python -m pip install pandas  

-Option 2:

Install Conda (Anaconda or Miniconda) for your OS.  
Create and activate an environment with Python 3.10+ and pandas:  

conda create -n searchppm python=3.10 pandas  
conda activate searchppm  

## Run

python SearchPPM.py
