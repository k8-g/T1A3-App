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


# Goes through each letter and checks if the guessed letter is in word then display letter if correct
    def check_letters(self):
        self._blanked_word = ""
        for letter in self._hangman_word:
            if letter in self._guesses:
                self._blanked_word += letter
            else:
                self._blanked_word += "_"
            self._blanked_word += " "

  # Goes through each letter and checks if the guessed letter is in word then displays blank if incorrect

# starts the game
    def start_game(self):
        #generates random word
        self._hangman_word = self.generate_word()
        # while game is playing
        while self._game_over == False:
            self.check_letters()
            print(self._blanked_word)
            user_letter = input ("Try guessing a letter.")
            self._guesses += user_letter
            
            
            #wip, still need to add number of guesses & set game over, plus other things.