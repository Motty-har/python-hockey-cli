from models.positions import Position

def list_positions():
    positions = Position.get_all()
    for position in positions:
        print(position)

def add_position():
    position = input("Please enter the position: ")
    type = input("Please enter the position type: ")
    position = Position.create(position, type)
    print(f'Success: {position}')

def update_position():
    pass

def delete_position():
    pass

def exit_program():
    print("Goodbye!")
    exit()