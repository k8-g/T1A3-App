# To install application:

### System Requirements:

- MacOS/Linux/Windows
- At least Python 3.9 & above
(I'm using Python 3.12.2)
- Program must be run in standard terminal window at least 80 characters wide for optimal viewing.

### Dependencies required:
- [Colored 2.2.4](https://pypi.org/project/colored/)
- [Rich](https://github.com/Textualize/rich?tab=readme-ov-file)
- [wonderwords 2.2.0](https://pypi.org/project/wonderwords/)

## To run application:
- Open terminal
- Make sure run.sh is executable: `chmod +x run.sh`
- Run `run.sh` command
----------------

The run.sh file has everything required to run this program, including checking what version of Python you have, creating a virtual environment, & installing packages/dependencies.

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

----
## How to use Hangman application:

Select one of the following options from the main menu and press 'Enter'.

    "Press 'Space' to start game"
    "Press 'S' to view stats"
    "Press '?' to display help"
    "Press 'Q' to exit game"
    Select one of the above and hit 'Enter'.
____
- **Press 'Space' to start game:**

    To start the game, press the `'Spacebar'` key and hit `'Enter'`. You will be asked to guess a letter, so press any letter you'd like to guess and then `'Enter'`. The game will tell you whether your guess is in the word or not. Try to guess all the letters before the Hangman is complete!

- If you want to quit the game at any time while playing, just press `'!' + 'Enter'`. This will end the game, then `'Q' + 'Enter'` to exit out of the program.
-----
-  **Press 'S' to view stats:**

    Here you can view your wins and losses! Press any key and  `'Enter'` to exit the stats page.
---
-  **Press 'Q' to exit game:**

    `'Q' + 'Enter'` exits the program. 
____
