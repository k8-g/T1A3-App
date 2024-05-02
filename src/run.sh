#!/bin/bash

# Make the scripts executable
chmod +x ./check_python.sh
chmod +x ./create_venv.sh
chmod +x ./install_packages.sh
# Run the check python script
./check_python.sh

# Check these are installed before running
./create_venv.sh

# Packages to be installed
./install_packages.sh

# Runs the program
python3 hangman.py