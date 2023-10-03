from helpers import (
    exit_program,
    list_positions,
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
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type E to exit the program:")
    print("Type P to view positions:")

def positions_submenu():
    print("Type B to go back")#need help with this

def player_submenu():
    print("Type B to go back")
    

def view_stats():
    pass



if __name__ == "__main__":
    main()
