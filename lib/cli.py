from helpers import (
    exit_program,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice is "E":#how to do upercase and lowercase
            exit_program()
        elif choice is "P":
            positions_submenu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type E to exit the program")

def positions_submenu():
    print("Type B to go back")#need help with this

def player_submenu():
    print("Type B to go back")
    

def view_stats():
    pass



if __name__ == "__main__":
    main()
