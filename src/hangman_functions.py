# imports
import os 
import hangman_screens
from Game import Game
from Stats import Stats
from rich.console import Console
from rich.markdown import Markdown



# Global varibles that can be called on from anywhere in this file
player_name = "Player"
stats = Stats(player_name)
stats.load_stats()
console = Console()

# Menu function, displays options that can be executed
def create_menu():
    # Uses Rich package to center text
    console.print("Press 'Space' to start game  |  Press 'S' to view stats",justify="center") 
    console.print("Press '?' to display help   |  Press 'Q' to exit game",justify="center") 
 
    # Asks the user for input, selecting one of the above options
    menu_selection = input("Select one of the above and hit 'Enter'.")
    # converts the user's selection into lowercase if they input as uppercase
    return menu_selection.lower()

# Function to clear screen
def clear_screen():
    # This will clear the screen between menus
    os.system("clear")

# Function to return to main menu after user inputs any key + Enter
def any_key_return_to_menu():
    # Waits for the user to input a key to acknowledge they have finished reading the help page
    user_input = input("Press any key to return to main menu.")
    # Clears the screen before returning to main menu
    clear_screen()

# Function to display at beginning of application
def display_intro():
    clear_screen()
    # Displays Hangman ASCII image loaded from hangman_screens file
    console.print(hangman_screens.intro_image)
    # Uses Rich package to have blinking text that is centered
    console.print("    WELCOME TO HANGMAN!", style="blink", justify="center")

# Function to display help info
def display_help():
    clear_screen()
    # HELP.md is shown with Markdown using Rich package
    with open("HELP.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)
    any_key_return_to_menu()

# Function to display stats page
def display_stats():
    clear_screen()
    print("Stats")
    print("Wins | Losses")
    print(f"{stats.get_wins()}    | {stats.get_losses()} ")
    any_key_return_to_menu()


# Function to start the game
def play_game():
    clear_screen()
    my_game = Game(stats)
    my_game.start_game()
    stats.save_stats()
