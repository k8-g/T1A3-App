from wonderwords import RandomWord

class Game:
    #Contructor
    def __init__(self):
        self._hangman_word = ""
        self._incorrect = 0
        self._guesses = ""
        self._blanked_word = ""
        self._word_generator = RandomWord()
        self._game_over = False
        


    # generates random word
    def generate_word(self):
        return self._word_generator.word(word_min_length=5, word_max_length=10)

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
            self._game_over = True
            print(f"Congratulations, you guessed it! It was \"{self._hangman_word}\".")


    #checks if user's guess letter is correct and updates screen
    def check_user_guess(self, _guess):
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
                self._game_over = True
                print("GAME OVER!")
                print(f"Sorry, you lost. The word was \"{self._hangman_word}\".")


# starts the game
    def start_game(self):
        #generates random word
        self._hangman_word = self.generate_word()
        self.check_letters()

        # while game is playing
        while self._game_over == False:
            print(self._blanked_word)
            user_guess = input ("Try guessing a letter.\n").lower().strip() 
            if len(user_guess) == 1:
                self.check_user_guess(user_guess)
            else:
                print("Please only select one letter.")
            self.check_letters()

        # remove spaces using strip from input