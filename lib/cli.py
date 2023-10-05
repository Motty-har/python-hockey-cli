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
    go_back
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
            if choice == "B":
                go_back()
            elif choice == "V":
                view_players_by_position()
            elif choice == "H":
                handle_positions()
                choice = input("> ")
                if choice == "B":
                    go_back()
                if choice == "A":
                    add_position()
                elif choice == "U":
                    update_position()
                elif choice == "D":
                    delete_position()
            else:
                print("Invalid choice")
        elif choice == "V":
            list_players()
            players_submenu()
            choice = input("> ")
            if choice == "A":
                add_player()
            elif choice == "U":
                update_player()
            elif choice == "D":
                delete_player()
            else:
                print("Invalid choice")
        elif choice == "S":
            view_stats()
            choice = input("> ")
            if choice == "P":
                find_player_by_name()
            elif choice == "G":
                goals_leaders()
            elif choice == "A":
                assists_leaders()
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type P to view positions:")
    print("Type V to view players:")
    print("Type S to view stats:")
    print("Type E to exit the program:")


def positions_submenu():
    print("Type B to go back:")#need help with this
    print("Type V to view players by position:")
    print("Type H to handle positions:")

def handle_positions():
    print("Type B to go back:")
    print("Type A to add a position:")
    print("Type U to update a position:")
    print("Type D to delete a position:")

def players_submenu():
    print("Type B to go back")
    print("Type A to add a player: ")
    print("Type U to update a player: ")
    print("Type D to delete a player")
    

def view_stats():
    print("Type B to go back")
    print("Type P to view by player")
    print("Type G to view goals leaders:")
    print("Type A to view assists leaders")



if __name__ == "__main__":
    main()
