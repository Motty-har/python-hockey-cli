from helpers import (
    exit_program,
    list_positions,
    add_position,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E":#how to do upercase and lowercase
            exit_program()
        elif choice == "P":
            list_positions()
            positions_submenu()
            choice = input("> ")
            if choice == "A":
                add_position()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type P to view positions:")
    print("Type E to exit the program:")
    
def positions_submenu():
    print("Type B to go back:")#need help with this
    print("Type A to add a position:")

def player_submenu():
    print("Type B to go back")
    

def view_stats():
    pass



if __name__ == "__main__":
    main()
