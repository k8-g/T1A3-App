# Imports of our own functions
from hangman_functions import display_help, display_intro, display_stats, play_game, create_menu



user_selection = ""

display_intro()
while user_selection != "q":
    user_selection = create_menu()
    if (user_selection == " "):
        print("Start game!")
        play_game()
    elif (user_selection == "s"):
        display_stats()
    elif (user_selection == "?"):
        display_help()
    elif (user_selection == "q"):
        print("Bye!")
    
    else:
        print("Please pick one of the above.")

print("Good Game!")