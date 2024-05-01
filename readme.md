# T1A3 - Terminal Application Assignment
## Kate Gerber's Text-Based Word Guessing Game/Hangman

### R3. Referenced Sources
<details>
<summary>Sources Links</summary>

- [Hangman image](https://www.google.com/search?sca_esv=f807be754d1cd3a2&q=hangman&tbm=isch&source=lnms&sa=X&sqi=2&ved=2ahUKEwih9L3pmuiFAxV1T2wGHUMWBMQQ0pQJegQICRAB&biw=1248&bih=662&dpr=2#imgrc=ecE6rYqZmYlRfM)
- [Image to ASCII Art converter](https://www.asciiart.eu/image-to-ascii?fbclid=IwZXh0bgNhZW0CMTAAAR08yyg_svulntnc3UI1XGw2Wuea9jSeOVbfEflhgXi45hgDOFl291kq2kU_aem_AYbxnqkTaRass8EeeWkuXmK7GzCK-6BE5pAZXviP1cAcJ4KOZkJbZhByOkrExaD7ADyerPMrMyRvi4z_Nrka2rEt)
- [Strip code](https://www.w3schools.com/python/ref_string_strip.asp)
- [wonderwords](https://pypi.org/project/wonderwords/)
- [Pytest](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest?fbclid=IwZXh0bgNhZW0CMTAAAR0R5irQ4ivfQU9jiogdVaP1VLqV8zg-dSEs9-kYAQsykKWJ6BQYcn16IJo_aem_AYbatc_krk9xhKD0S8a02RKU8GCWbZlcF2zQ0kljdqGmdtt0QFVlcm85t2tK5oYdz2QvPmBrRlCDBfIQq7VcJjuX)
- [Rich](https://github.com/Textualize/rich)
- [Colored](https://dslackw.gitlab.io/colored/)

</details>

## R4. GitHub Repository Link
- [GitHub T1A3 App Link](https://github.com/k8-g/T1A3-App)

## R5. Code Style
PEP8 Style
- snake_case used for majority of code
- Camel_case used for Classes
- Tabs used for indentation, instead of four spaces
- Comments capitilised with one space between # and comment
- """ on new line at end

## R6. Develop a list of features that will be included in the application. 

### Main features of the app:
- Main menu & it's executable options
    - 'Start game', 'View stats', 'Display Help', 'Quit game'
- 'View stats' page; shows saved wins & losses count
- 'Hangman Help' page; basic user how-to-play text tutorial
- The game itself; 
    - Displays empty Hangman gallows (with no body)
    - Loads a randomly generated word from wonderwords
    - Converts the randomly generated word into a blanked "hidden" word
    - Prompts the user to guess a letter
    - Loops through all letters in randomly generated word
    - Checks if user's guess is correct, displays correct guess message 
    - Checks if user's guess is incorrect, displays incorrect guess message
    - Saves what letters user has guessed in hidden '_guess' list
    - Updates Hangman drawing if incorrect, adding a body part each time
    - Checks if game is over (incorrect count = 6)
    - Displays Win or Lose message
    - Saves every win & loss to 'View Stats' page
    - Quit game while playing, doesn't save game as win or loss
    - Screen flashes if user loses game
- Quit program

#### Error Handling:

    - if user inputs anything other than options shown in menu
    - if user inputs uppercase letters
    - if user inputs more than one character while guessing
    - if user inputs any spaces while guessing

#### File Handling:
- Saves wins and losses in stats.csv  file
- Loads wins and losses to 'View Stats' page
___
### Main Menu: 

The main menu screen loads at the beginning of the program. It shows a 'Hangman' ACSII text image, a blinking 'WELCOME TO HANGMAN!' message, and lists the following options. The program waits for the user to input their selection.

    1. "Press 'Space' to start game"
    2. "Press 'S' to view stats"
    3. "Press '?' to display help"
    4. "Press 'Q' to exit game"
    Select one of the above and hit 'Enter'.

The main menu is created using a display menu function (create_menu in hangman_functions.py) and the user input menu function (display_intro in hangman.py). If the user inputs anything other than the above options, the program gives a warning message asking the user to "Select one of the above and hit 'Enter'." (see else: in display_intro in hangman.py)

If the user inputs their option in uppercase, there is an error handling code that converts their input into lowercase, so the program won't break and will continue as normal (see end of create_menu function in hangman_functions.py).
___
### Playing the game:

After the player presses 'Spacebar' + 'Enter', the game starts. A random word is generated using the [wonderwords package](https://pypi.org/project/wonderwords/), which is then displayed as a blanked out word, showing the hidden letters as underscores, for example, the word 'feline' would be displayed as '_ _ _ _ _ _'. An empty 'Hangman' gallows text image is displayed as well.

Two functions operate to start the game; play_game in hangman_functions.py & start_game in Game.py. The first clears the screen and loads the game, whilst the  second draws the empty gallows, generates the random word to be guessed and replaces the letters in the words to be displayed as underscores with spaces beside them to seperate them. 

The player then can input a letter followed by the 'Enter' key, and the game will let the player know if their guess is in the word or an incorrect guess. It does this by running a check_letters function which checks if the inputted letter is in the word. 

If the player guesses a letter correctly, that letter is then converted from the corresponding underscore into the guessed letter in the displayed blanked word. A message will also be displayed telling the player that the letter they have guessed is correct. They then can guess again.

If the player guesses incorrectly, a message displays saying that the letter guessed is not in the word and the 'Hangman' ASCII image will be updated to reflect the next stage of the Hanged man. A function will also add a count to the incorrect guesses count. 

If they have guessed the letter before, a message is displayed letting the user know that they've already guessed that letter, and the game will treat that guess as a turn, penalising the user if it's incorrect. 

The player can continue guessing until either they have guessed all the hidden letters, or until the Hangman drawing is complete, which is 6 incorrect guesses count.

A series of functions runs after every guess. First, it checks the letter if it's in the word with an outcome for True (correct) or False (incorrect). If the guessed letter is in the word, it updates the display to reflect this as well as if it's incorrect. There is also a function that converts the user input into lowercase and stips any accidental or excess spaces, so that the game will function as normal even if the input is uppercase or if the user inputs any spaces. As well as a function that tells the user to only select one letter if they accidentally type more than one letter.

In between all these turns, a function is called from the OS to clear the screen.

Once the player has guessed all the letters, a win_game function runs, telling the user 'Congratulations, you guessed it! It was "_____" and it adds your win to the wins stats count, which can be viewed on the 'View Stats' page, once you have played a game to completion.

If the user fails to guess before the 'Hangman' drawing is completed, the game ends and the game saves your game as a loss count, which can also be viewed in the 'View Stats' page. There is a function that checks if the game is over by checking the incorrect guesses count and once this reaches 6, it ends the game, and a terminal bell/screen flash occurs.

The user can exit the game at any point by pressing '!' + 'Enter'. Exiting the game doesn't save anything to the 'View Stats' page and the player can choose again from the main menu.

### View Stats
Pressing 'S' + 'Enter' takes you to a 'View Stats' page, where the user is able to see the wins and losses of every time they've played. The outcome of the game is saved after every game via file handling and is viewable in the 'View Stats' page. 

If the player exits the program and reruns the program, they can see the previous stats in the 'View Stats' page.

### Help page
Pressing '?' + 'Enter' takes the user to a help display page, where they can find a basic how-to-play the game explaination (HELP.md file).

### Quit Game
Pressing 'Q' + 'Enter' quits the program altogether.

## R7. Implementation Plan
[Trello Board](https://trello.com/invite/b/2KkDIwnm/ATTI8c7dcc244337075ee0527f62c31d103895FB879E/t1a3-terminal-application-assignment-checklist)

## R8. Help Documentation

See [Help Documentation.md](docs/Help%20Documentation.md) for how to install and use app


#### Packages used:
- [Colored](https://pypi.org/project/colored/)
    - Allows colours in program

- [Rich](https://github.com/Textualize/rich)
    - Allows rich text formatting in HELP.md
    - Centers text in code

- [WonderWords](https://pypi.org/project/wonderwords/)
    - Generates random word for game

- OS (built-in Python module)
    - clear screen function
    - file handling

- [Pytest](https://docs.pytest.org/en/stable/)
    - Error handling
    - Testing

