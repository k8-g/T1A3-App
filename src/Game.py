# Imports from dependencies/packages/files
import os
from colored import Fore, Back, Style
from rich.console import Console
from wonderwords import RandomWord
import hangman_screens


console = Console()

# Class for Game objects
class Game:
    # Constructors
    def __init__(self, _stats=None):
        self._hangman_word = ""
        self._incorrect = 0
        self._guesses = ""
        self._blanked_word = ""
        self._word_generator = RandomWord()
        self._game_over = False
        self._stats = _stats
        

    # Generates random word to be guessed
    def generate_word(self):
        return self._word_generator.word(word_min_length=5, word_max_length=8)

    # Getter to get blanked word
    def get_blanked_word(self):
        return self._blanked_word

# Goes through each letter and checks if the guessed letter is in word then displays letter if correct, displays blank if incorrect
    def check_letters(self):
        word_guessed = True
        self._blanked_word = ""
        for letter in self._hangman_word:
            if letter in self._guesses:
                self._blanked_word += letter
            else:
                self._blanked_word += "_"
                word_guessed = False
            self._blanked_word += " "
        # If every letter has been guessed, then the game ends
        if word_guessed == True:
            self.win_game()
    
    # Line break function
    def line_break(self):
        print("---------------------------------------------------------")

    # Win game function
    def win_game(self):
        self._game_over = True
        print(f"{Fore.green}Congratulations, you guessed it! It was \"{self._hangman_word}\".{Style.reset}")
        self.line_break()
        self._stats.add_win()
        
    # Lose game function
    def lose_game(self):
        self._game_over = True
        self.line_break()
        print(f"{Fore.cyan}GAME OVER!{Style.reset}")
        # Terminal bell/visual bell when you lose the game
        print("\a")
        print(f"{Fore.red}Sorry, you lost. The word was \"{self._hangman_word}\".{Style.reset}")
        self._stats.add_loss()

    # Checks if user's guess letter is correct and updates screen
    def check_user_guess(self, _guess):
        self.line_break()
        # If they guess a letter they've already guessed, this warning comes up and still counts as a turn
        if _guess in self._guesses:
            print(f"{Fore.magenta}You've already guessed {_guess}.{Style.reset}")
        else: 
            # If they haven't guessed the letter before, it gets added to the guess list which is hidden from user
            self._guesses += _guess

        if _guess not in self._hangman_word:
            # Incorrect guess; message displays & incorrect guess count goes up +1, then user can guess again if the incorrect count is under 6
            self._incorrect += 1
            print(f"{Fore.red}Sorry, {_guess} isn't in this word.{Style.reset}")
            # If the incorrect count gets to 6, the game ends
            if self._incorrect == 6:
                self.lose_game()
        else:
            # Correct guess; prints display message, Nothing else happens and user can guess again
            print(f"{Fore.green}Yay! You guessed correctly!{Style.reset}")   
        self.line_break()

    # Tells when to draw what hangman gallows stage by using the number corresponding to the hangman stage 0 (empty gallows) - 6 (completed hangman body)
    def draw_hangman(self):
        print(hangman_screens.hangman_images [self._incorrect])
        print("\n")

    # Starts the game
    def start_game(self):
        self.draw_hangman() 
        # Generates random word
        self._hangman_word = self.generate_word()
        # Displays dashes for the length of the word
        print("_ "*len(self._hangman_word))
        
        # While game is playing
        # While game is not over/ while game over = false
        while self._game_over == False:
            # Prints blanked out word
            print(self._blanked_word)
            # Ask for input and converts input into lowercase and strips any spaces inputted
            user_guess = input ("Try guessing a letter.\n").lower().strip()
            # Clears screen
            os.system("clear")
            # if the length of the user's input is one character
            if len(user_guess) == 1:
                # Quits the game if user types '!'
                if user_guess == "!":
                    # Tells game to end/changes game over = false to true
                    self._game_over = True
                    # Prints game ended message
                    console.print("[bold] GAME ENDED [/bold]")
                else:
                    # Otherwise turn continues as normal
                    self.check_user_guess(user_guess)  
            else:
                # If user inputs more than one character, this warning comes up
                self.line_break()
                print(f"{Fore.magenta}Please only select one letter.{Style.reset}")
                self.line_break()
            self.check_letters()
            self.draw_hangman()
        self.line_break()
