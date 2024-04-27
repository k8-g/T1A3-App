#!/bin/bash

# Check these are installed before running
python3 -m venv .venv
source .venv/bin/activate

# Packets to be installed
pip3 install pytest
# pip3 install colored
pip3 install wonderwords
pip3 install rich

# Runs the program
python3 hangman.py