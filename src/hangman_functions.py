import os


def display_intro():
    # this will clear the screen between menus
    os.system("clear")
    print("Welcome to Hangman!")

# Function to display help info
def display_help():
    os.system ("clear")
    print("This will print some help info for how to play the game.") 
    #Wait for the user to input a key to acknowledge they have finished the help page
    user_input = input("Press any key to return to main menu.")
    os.system ("clear")

def display_stats():
    os.system ("clear")
    print("Stats")
    user_input = input("Press any key to return to main menu.")
    os.system ("clear")

def play_game():
    os.system("clear")
    print("")