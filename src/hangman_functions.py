import os

def any_key_return_to_menu():
    # Wait for the user to input a key to acknowledge they have finished the help page
    user_input = input("Press any key to return to main menu.")
    # Clears the screen before returning to menu
    os.system ("clear")

def display_intro():
    # this will clear the screen between menus
    os.system("clear")
    print("Welcome to Hangman!")

# Function to display help info
def display_help():
    os.system ("clear")
    print("This will print some help info for how to play the game.") 
    any_key_return_to_menu()

def display_stats():
    os.system ("clear")
    print("Stats")
    any_key_return_to_menu()

def play_game():
    os.system("clear")
    print("")
