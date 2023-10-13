from models.positions import Position
from models.player import Player

positions = Position.get_all()
players = Player.get_all()

def list_positions():
    for index, position in enumerate(positions):
        print(f"{index + 1}. {position.position}, {position.type}")

def view_players_by_position(position_submenu):
    num = input("Enter the number of the position: ")
    if player := positions[int(num) - 1]:
        for index, player in enumerate(Position.players(player)):
            print(f'{index + 1}. Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
    else:
        print(f'Position {num} not found')
    
    handle_in_positions(num, position_submenu)

def handle_in_positions(num, position_submenu):
    while True:
        inside_positions()
        choice = input("> ")
        if choice == "A":
            add_in_position(num)
        if choice == "B":
            position_submenu()
        else:
            print("Invalid choice")

def add_in_position(num):
    name = input("Enter the player's name: ")
    number = int(input("Enter the player's number: "))
    goals = int(input("Enter the players goal total: "))
    assists = int(input("Enter the players assist total: "))
    try:
        player = Player.create(name, number, goals, assists, positions[int(num) - 1].id)
        print(f'Success: Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
    except Exception as exc:
        print("Error creating player: ", exc)

def inside_positions():
    print("Type A to add a player in this position")
    print("Type B to go back")

#doesnt add to the position list right away
def add_position():
    position = input("Please enter the position: ")
    type = input("Please enter the position type: ")
    position = Position.create(position, type)
    print(f'Success: Position: {position.position}, Type: {position.type}')

def update_position():
    num = input("Enter the number of the position: ")
    if pos := positions[int(num) - 1]:
        try:
            position = input("Enter the updated position: ")
            pos.position = position
            type = input("Enter the updated position type: ")
            pos.type = type
            pos.update()
            print(f'Success: {pos.position, pos.type}')
        except Exception as exc:#what is the functinality of this
            print("Error updating position: ", exc)
    else:
        print(f'Position {num} not found)')

def delete_position():
    num = input("Enter the position's number: ")
    if position := positions[int(num) - 1]:
        position.delete()
        print(f'Position {num} deleted')
    else:
        print(f'Postion {num} not found')

def list_players():
    for index, player in enumerate(players):
        print(f'{index + 1}. Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}') #want to write out the players position

def add_player():
    name = input("Enter the player's name: ")
    number = int(input("Enter the player's number: "))
    goals = int(input("Enter the players goal total: "))
    assists = int(input("Enter the players assist total: "))
    position_id = int(input("Enter the player's position number: "))
    try:
        player = Player.create(name, number, goals, assists, positions[position_id - 1].id)
        print(f'Success: Name: {player.name}, #{player.number}, Goals: {player.goals}, Assists: {player.assists}')
    except Exception as exc:
        print("Error creating player: ", exc)

def add_player_in_positoin():
    pass

def update_player():
    id_ = int(input("Enter the number of the player: "))
    if player := players[id_ -1]:
        try:
            name = input("Enter the players updates name: ")
            player.name = name
            number = input("Enter players updated number: ")
            player.number = number
            goals = input("Enter the players new goal total: ")
            player.goals = goals 
            assists = input("Enter the players new assist total: ")
            player.assists = assists
            position_id = int(input("Enter the position number: "))
            player.position_id = position_id
            
            player.update()
            print(f"Success: {player}")
        except Exception as exc:
            print('Error updating player:', exc)
    else:
        print(f'Player {id_} not found')

def delete_player():
    num = input("Enter the players's number: ")
    if player := players[int(num) - 1]:
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
    pass

def assists_leaders():
    pass

def exit_program():
    print("Goodbye!")
    exit()