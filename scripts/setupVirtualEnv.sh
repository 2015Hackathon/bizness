#!/bin/sh

# This script will create a Python 2.6 virtual environment
# with dependencies (see requirements.txt) in the project
# root directory.

virtualenv --distribute --python=/usr/bin/python2.7 ../venv
source ../venv/bin/activate
pip install -r requirements.txt
deactivate