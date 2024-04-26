def create_menu():
    print("Press 'Space Key' to start game \n") 
    print("Press S to view stats \n")  
    print("Press ? to display help \n") 
    print("Press Q to exit game")
 

    menu_selection = input("Press one of the above :)")
    return menu_selection

user_selection = ""

while user_selection != "Q":
    user_selection = create_menu()

    if (user_selection == " "):
        print("Start game!")
    elif (user_selection == "S"):
        print("View stats")
    elif (user_selection == "?"):
        print("Help Display")
    elif (user_selection == "Q"):
        print("Bye!")
    
    else:
        print("Please pick one of the above.")

print("Good Game!")