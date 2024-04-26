# Imports of our own functions
from hangman_functions import display_help

def create_menu():
    print( "Welcome to Hangman! \n")
    print("Press 'Space Key' to start game \n") 
    print("Press S to view stats \n")  
    print("Press ? to display help \n") 
    print("Press Q to exit game")
 

    menu_selection = input("Select one of the above and hit enter.")
    return menu_selection.lower()

user_selection = ""

while user_selection != "q":
    user_selection = create_menu()
    if (user_selection == " "):
        print("Start game!")
    elif (user_selection == "s"):
        print("View stats")
    elif (user_selection == "?"):
        display_help()
    elif (user_selection == "q"):
        print("Bye!")
    
    else:
        print("Please pick one of the above.")

print("Good Game!")