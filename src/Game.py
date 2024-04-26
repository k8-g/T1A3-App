from wonderwords import RandomWord

class Game:
    #Contructor
    def __init__(self):
        self._hangman_word = ""
        self._incorrect = 0
        self._guesses = ""
        self._blanked_word = ""
        self._word_generator = RandomWord()

    def generate_word(self):
        return self._word_generator.word(word_min_length=5, word_max_length=10)
