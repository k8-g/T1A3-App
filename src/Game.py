from wonderwords import RandomWord
import hangman_screens
import os

class Game:
    #Contructor
    def __init__(self, _stats=None):
        self._hangman_word = ""
        self._incorrect = 0
        self._guesses = ""
        self._blanked_word = ""
        self._word_generator = RandomWord()
        self._game_over = False
        self._stats = _stats
        


    # generates random word
    def generate_word(self):
        return self._word_generator.word(word_min_length=5, word_max_length=8)

    # Getter
    def get_blanked_word(self):
        return self._blanked_word


# Goes through each letter and checks if the guessed letter is in word then display letter if correct, displays blank if incorrect
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
        # if the whole word has been guessed, then the game ends
        if word_guessed == True:
            self.win_game()
    
    def line_break(self):
        print("---------------------------------------------------------")


    # win game function
    def win_game(self):
        self._game_over = True
        print(f"Congratulations, you guessed it! It was \"{self._hangman_word}\".")
        self.line_break()
        self._stats.add_win()
        


    # lose game function
    def lose_game(self):
        self._game_over = True
        self.line_break()
        print("GAME OVER!")
        # terminal bell/visual bell when you lose the game
        print("\a")
        print(f"Sorry, you lost. The word was \"{self._hangman_word}\".")
        self._stats.add_loss()

    #checks if user's guess letter is correct and updates screen
    def check_user_guess(self, _guess):
        self.line_break()
        # if they guess a letter they've already guessed, this warning comes up and still counts as a turn
        if _guess in self._guesses:
            print(f"You've already guessed {_guess}.")
        else: 
            # if they haven't guessed the letter before, it gets added to the guess list
            self._guesses += _guess

        if _guess not in self._hangman_word:
            #incorrect guess
            self._incorrect += 1
            print(f"Sorry, {_guess} isn't in this word.")
            if self._incorrect == 6:
                self.lose_game()
        else:
            print("Yay! You guessed correct!")   
        self.line_break()

    # tells when to draw what hangman stage
    def draw_hangman(self):
        print(hangman_screens.hangman_images [self._incorrect])
        print("\n")



    # starts the game
    def start_game(self):
        self.draw_hangman() 
        #generates random word
        self._hangman_word = self.generate_word()
        # displays dashes for the length of the word
        print("_ "*len(self._hangman_word))
        


        # while game is playing
        while self._game_over == False:
            print(self._blanked_word)
            # converts input into lowercase and strips any spaces inputted
            user_guess = input ("Try guessing a letter.\n").lower().strip() 
            os.system("clear")
            if len(user_guess) == 1:
                # quit the game if user types !
                if user_guess == "!":
                    self._game_over = True
                    print("GAME ENDED")
                else:
                    # otherwise turn continue as normal
                    self.check_user_guess(user_guess)  
            else:
                self.line_break()
                print("Please only select one letter.")
                self.line_break()

            self.check_letters()
            self.draw_hangman()
        self.line_break()
