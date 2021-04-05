# Federated-learning-MI
Federated learning using Pysyft and Duet for Medical Imaging example. 

the dataset is https://www.kaggle.com/andrewmvd/medical-mnist

The course follows OpenMined Syft framework.

## Env setup

### Prerequisites

1. Python Version 3 check with:
`
python3 --version
`
Python venv should be installed

2. virtualenv installed
`
virtualenv -h
`
If not installed install on linux with:
`
sudo apt update && sudo apt install virtualenv
`

### Getting started
1. create a virtual environment with **virtualenv** as 
`
virtualenv -p python3 env-name
`
with **conda** as 
`
conda create --name env-name
`
replace env-name with environment name of your choice

2. Activate virtual environment **virtualenv**
`
source env-name/bin/activate
`
 or  **conda**
`
conda activate env-name
`
3. Install Dependencies
`
pip install -r requirements.txt
`
4. Install syft by 
`
pip install git+https://github.com/OpenMined/PySyft@dev#egg=syft
`


