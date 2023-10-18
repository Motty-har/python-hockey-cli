from models.position import Position
from models.player import Player

players = Player.get_all()

def list_positions():
    for index, position in enumerate(Position.get_all()):
        print(f"{index + 1}. {position.position}, {position.type}")

def view_players_by_position(handle_positions):
    num = input("Enter the number of the position: ")
    if player := Position.get_all()[int(num) - 1]:
        for index, player in enumerate(Position.players(player)):
            print(f'{index + 1}. Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
    else:
        print(f'Position {num} not found')
    
    handle_in_positions(num, handle_positions)

def handle_in_positions(num, handle_positions):
    while True:
        inside_positions()
        choice = input("> ")
        if choice == "A":
            add_in_position(num)
        elif choice == "B":
            handle_positions()
        else:
            pass
        

def add_in_position(num):
    name = input("Enter the player's name: ")
    number = int(input("Enter the player's number: "))
    goals = int(input("Enter the players goal total: "))
    assists = int(input("Enter the players assist total: "))
    try:
        player = Player.create(name, number, goals, assists, Position.get_all()[int(num) - 1].id)
        print(f'Success: Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
    except Exception as exc:
        print("Error creating player: ", exc)

def inside_positions():
    print("Type A to add a player in this position")
    print("Type B to go back")


def add_position():
    position = input("Please enter the position: ")
    type = input("Please enter the position type: ")
    position = Position.create(position, type)
    print(f'Success: Position: {position.position}, Type: {position.type}')

def update_position():
    list_positions()
    num = input("Enter the number of the position: ")
    if pos := Position.get_all()[int(num) - 1]:
        try:
            position = input("Enter the updated position: ")
            pos.position = position
            type = input("Enter the updated position type: ")
            pos.type = type
            pos.update()
            print(f'Success: Position: {pos.position}, Type: {pos.type}')
        except Exception as exc:
            print("Error updating position: ", exc)
    else:
        print(f'Position {num} not found)')

def delete_position():
    print("Warning: Deleting the position will also delete the players that play it!")
    list_positions()
    num = input("Enter the position's number: ")
    if position := Position.get_all()[int(num) - 1]:
        delete_player_in_position(position)
        position.delete()
        print(f'Position {num} deleted')
    else:
        print(f'Postion {num} not found')

def delete_player_in_position(position):
    if player := Player.find_by_position_id(position.id):
        player.delete()

def list_players():
    for index, player in enumerate(Player.get_all()):
        print(f'{index + 1}. Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')

def add_player():
    name = input("Enter the player's name: ")
    number = int(input("Enter the player's number: "))
    goals = int(input("Enter the players goal total: "))
    assists = int(input("Enter the players assist total: "))
    list_positions()
    position_id = int(input("Enter the player's position number: "))
    try:
        player = Player.create(name, number, goals, assists, Position.get_all()[position_id - 1].id)
        print(f'Success: Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
    except Exception as exc:
        print("Error creating player: ", exc)

def update_player():
    list_players()
    id_ = int(input("Enter the number of the player: "))
    if player := Player.get_all()[id_ -1]:
        try:
            name = input("Enter the players updates name: ")
            player.name = name
            number = int(input("Enter the players updated number: "))
            player.number = number
            goals = int(input("Enter the players new goal total: "))
            player.goals = goals 
            assists = int(input("Enter the players new assist total: "))
            player.assists = assists
            list_positions()
            position_id = int(input("Enter the position number: "))
            player.position_id = position_id
            player.update()
            print(f'Success: Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
        except Exception as exc:
            print('Error updating player:', exc)
    else:
        print(f'Player {id_} not found')

def delete_player():
    list_players()
    num = input("Enter the players's number: ")
    if player := Player.get_all()[int(num) - 1]:
        player.delete()
        print(f'Player {num} deleted')
    else:
        print(f'Player {num} not found')

def find_player_by_name():
    name = input("Enter the players name: ")
    player = Player.find_by_name(name)
    print(f'Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}') if player else(
        print(f'{name} not found')
    )

def goals_leaders():
    goal_leader = sorted(Player.get_all(), key=lambda player: player.goals, reverse=True)
    num = 1
    for player in goal_leader:
        print(f'{num}. Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
        num += 1

def assists_leaders():
    assist_leader = sorted(Player.get_all(), key=lambda player: player.assists, reverse=True)
    num = 1
    for player in assist_leader:
        print(f'{num}. Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
        num += 1

def exit_program():
    print("Goodbye!")
    exit()