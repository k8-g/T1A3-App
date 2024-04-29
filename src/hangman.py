# Imports of own functions
from hangman_functions import display_help, display_intro, display_stats, play_game, create_menu


user_selection = ""

# Displays intro menu
display_intro()
# while user's selection isn't equal to 'q'
while user_selection != "q":
    user_selection = create_menu()
    # If user selects 'Spacebar', the game starts
    if (user_selection == " "):
        print("Start game!")
        play_game()
    # If user selects 'S', the 'View Stats' page loads
    elif (user_selection == "s"):
        display_stats()
    # If the user selects '?', the 'Help Info' page loads
    elif (user_selection == "?"):
        display_help()
    # If the user selects 'q', it quits the application
    elif (user_selection == "q"):
        print("Bye!")
    # If user inputs anything other than the above options, this warning message comes up
    else:
        print("Please pick one of the above.")

print("Good Game!")