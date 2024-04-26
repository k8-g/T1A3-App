import os

# Function to display help info
def display_help():
    #this will clear the screen between menus
    os.system ("clear")
    print("This will print some help info for how to play the game.") 
    #Wait for the user to input a key to acknowledge they have finished the help page
    user_input = input("Press any key to return to main menu.")
    os.system ("clear")

def play_game():
    print("")