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
    pass

def update_player():
    pass

def delete_player():
    pass

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