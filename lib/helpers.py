from models.positions import Position
from models.player import Player

def list_positions():
    positions = Position.get_all()
    for position in positions:
        print(position)

def view_by_position():
    pass

def add_position():
    position = input("Please enter the position: ")
    type = input("Please enter the position type: ")
    position = Position.create(position, type)
    print(f'Success: {position}')

def update_position():#need help with this function
    id_ = input("Enter the position's id: ")
    if pos := Position.find_by_id(id_):
        try:
            position = input("Enter the updated position: ")
            pos.position = position
            type = input("Enter the position type: ")
            position.type = type

            pos.update()
            print(f'Success: {pos}')
        except Exception as exc:#what is the functinality of this
            print("Error updating position: ", exc)
    else:
        print(f'Position ({id_} not found)')

def delete_position():
    id_ = input("Enter the position's id: ")
    if position := Position.find_by_id(id_):
        position.delete()
        print(f'Position {id_} deleted')
    else:
        print(f'Postion {id_} not found')

def list_players():
    players = Player.get_all()
    for player in players:
        print(player)

def add_player():
    name = input("Enter the player's name: ")
    number = input("Enter the player's number: ")
    goals = input("Enter the players goal total: ")
    assists = input("Enter the players assist total: ")
    position_id = int(input("Enter the player's position id:"))
    try:
        player = Player.create(name, number, goals, assists, position_id)
        print(f'Success: {player}')
    except Exception as exc:
        print("Error creating player: ", exc)

def update_player():
    id_ = input("Enter the players id: ")
    if player := Player.find_by_id(id_):
        try:
            name = input("Enter the players new name: ")
            player.name = name
            number = input("Enter players new number: ")
            player.number = number
            goals = input("Enter the players new goal total: ")
            player.goals = goals 
            assists = input("Enter the players assist total: ")
            player.assists = assists
            position_id = int(input("Enter employees new position id: "))
            player.position_id = position_id
            
            player.update()
            print(f"Success: {player}")
        except Exception as exc:
            print('Error updating player:', exc)
    else:
        print(f'Employee {id_} not found')

def delete_player():
    id_ = input("Enter the players's id: ")
    if player := Player.find_by_id(id_):
        player.delete()
        print(f'Player {id_} deleted')
    else:
        print(f'Player {id_} not found')

def find_player_by_name():
    pass

def goals_leaders():
    pass

def assists_leaders():
    pass

def go_back():
    pass

def exit_program():
    print("Goodbye!")
    exit()