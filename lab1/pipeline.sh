#!/bin/bash
sudo apt install python3-sklearn.datasets
sudo apt install python3-sklearn.model_selection
sudo apt install python3-sklearn.linear_model
sudo apt install python3-preprocessing
sudo apt install python3-numpy
sudo apt install python3-pickle

python3 data_creation.py
python3 data_preprocessing.py
python3 model_preparation.py
python3 model_testing.py
