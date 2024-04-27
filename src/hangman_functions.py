# imports
import os 
import hangman_screens
from Game import Game
from Stats import Stats
from rich.console import Console
from rich.markdown import Markdown



# global varibles
player_name = "Player"
stats = Stats(player_name)
stats.load_stats()

# Function to clear screen
def clear_screen():
    # this will clear the screen between menus
    os.system("clear")

# function to return to main menu after user says so
def any_key_return_to_menu():
    # Wait for the user to input a key to acknowledge they have finished the help page
    user_input = input("Press any key to return to main menu.")
    # Clears the screen before returning to menu
    clear_screen()

# Function to display at beginning of application
def display_intro():
    clear_screen()
    print(hangman_screens.intro_image)

# Function to display help info
def display_help():
    clear_screen()
    console = Console()
    with open("HELP.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)
    print("This will print some help info for how to play the game.") 
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
