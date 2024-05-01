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
            # Incorrect guess
            self._incorrect += 1
            print(f"Sorry, {_guess} isn't in this word.")
            if self._incorrect == 6:
                self.lose_game()
        else:
            # Correct guess
            print(f"{Fore.green}Yay! You guessed correct!{Style.reset}")   
        self.line_break()

    # Tells when to draw what hangman gallows stage 
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
        while self._game_over == False:
            print(self._blanked_word)
            # Converts input into lowercase and strips any spaces inputted
            user_guess = input ("Try guessing a letter.\n").lower().strip() 
            os.system("clear")
            if len(user_guess) == 1:
                # Quits the game if user types '!'
                if user_guess == "!":
                    self._game_over = True
                    console.print("[bold] GAME ENDED [/bold]")
                else:
                    # Otherwise turn continues as normal
                    self.check_user_guess(user_guess)  
            else:
                # If user inputs more than one character, this warning comes up
                self.line_break()
                print("Please only select one letter.")
                self.line_break()
            self.check_letters()
            self.draw_hangman()
        self.line_break()
