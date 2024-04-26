from wonderwords import RandomWord

class Game:
    #Contructor
    def __init__(self):
        self._hangman_word = ""
        self._incorrect = 0
        self._guesses = ""
        self._blanked_word = ""
        self._word_generator = RandomWord()


    # generates random word
    def generate_word(self):
        return self._word_generator.word(word_min_length=5, word_max_length=10)

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


    def start_game(self):
        self._hangman_word = self.generate_word()
        self.check_letters()
        print(self._blanked_word)