import pytest 

from Game import Game

# def test_display_blanked_word():
    # my_game = Game()

    

def test_default_initial_value():
    my_game = Game()
    assert my_game._incorrect == 0


def test_check_letters():
    my_game = Game()
    my_game._guesses = "e"
    my_game._hangman_word = "feline"
    my_game.check_letters()
    assert my_game.get_blanked_word() == "_ e _ _ _ e "


def test_check_letters_incorrect():
    my_game = Game()
    my_game._guesses = "t"
    my_game._hangman_word = "feline"
    my_game.check_letters()
    assert my_game.get_blanked_word() == "_ _ _ _ _ _ "

def test_check_letters_multiple():
    my_game = Game()
    my_game._guesses = "ti"
    my_game._hangman_word = "feline"
    my_game.check_letters()
    assert my_game._blanked_word == "_ _ _ i _ _ "