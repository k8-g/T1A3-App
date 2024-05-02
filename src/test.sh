#!/bin/bash

chmod +x ./check_python.sh
chmod +x ./create_venv.sh
chmod +x ./install_packages.sh

./check_python.sh
./create_venv.sh
./install_packages.sh

# Tests the program
pytest