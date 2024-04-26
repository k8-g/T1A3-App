#!/bin/bash

# Check these are installed before running
python3 -m venv .venv
source .venv/bin/activate

pip3 install colored
pip3 install wonderwords

python3 application.py