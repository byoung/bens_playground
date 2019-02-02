#!/bin/bash

# A script to setup your python environment
# Assumes you have a global python configured already
# Credit to the site below for a simple way of setting up your env
# https://anbasile.github.io/programming/2017/06/25/jupyter-venv/

# Both
python -m venv python_env

# Linux
source python_env/bin/activate

# Windows
source python_env/Scripts/activate

# Both
pip install ipykernel
ipython kernel install --user --name=python_env
