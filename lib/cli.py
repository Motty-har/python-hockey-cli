from helpers import (
    exit_program,
    list_positions,
    view_players_by_position,
    add_position,
    update_position,
    delete_position,
    list_players,
    add_player,
    update_player,
    delete_player,
    goals_leaders,
    assists_leaders,
    find_player_by_name,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E":#how to do upercase and lowercase
            exit_program()
        elif choice == "P":
            handle_positions()
        elif choice == "V":
            handle_view_players()
        elif choice == "S":
            handle_view_stats()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type P to view positions:")
    print("Type V to view players:")
    print("Type S to view stats:")
    print("Type E to exit the program:")

def handle_positions():
    while True:
       list_positions()
       positions_submenu()
       choice = input("> ")
       if choice == "V":
            view_players_by_position(positions_submenu)   
       elif choice == "H":
            crud_positions()
       elif choice == "B":
            main()
       else:
            print("Invalid choice")
       
def positions_submenu():
    print("Type B to go back:")
    print("Type V to view players by position:")
    print("Type H to handle positions:")

def crud_positions():
    while True:
        edit_positions()
        choice = input("> ")
        if choice == "A":
            add_position()
        elif choice == "U":
            update_position()
        elif choice == "D":
            delete_position()
        elif choice == "B":
            handle_positions()
        else:
            print("Invalid choice")

def edit_positions():
    print("Type B to go back:")
    print("Type A to add a position:")
    print("Type U to update a position:")
    print("Type D to delete a position:")
       
def handle_view_players():
    while True:
        list_players()
        players_submenu()
        choice = input("> ")
        if choice == "A":
            add_player()
        elif choice == "U":
            update_player()
        elif choice == "D":
            delete_player()
        elif choice == "B":
            main()
        else:
            print("Invalid choice")

def players_submenu():
    print("Type B to go back")
    print("Type A to add a player: ")
    print("Type U to update a player: ")
    print("Type D to delete a player")

def handle_view_stats():
    while True:
        view_stats()
        choice = input("> ")
        if choice == "P":
            find_player_by_name()
        elif choice == "G":
            goals_leaders()
        elif choice == "A":
            assists_leaders()
        elif choice == "B":
            main()
        else:
            print("Invalid choice")

def view_stats():
    print("Type B to go back")
    print("Type P to view by player")
    print("Type G to view goals leaders:")
    print("Type A to view assists leaders")

if __name__ == "__main__":
    main()
