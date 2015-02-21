#!/bin/bash

rm -rf venv/
virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 venv
source venv/bin/activate
pip install -r requirements.freeze.txt --allow-all-external