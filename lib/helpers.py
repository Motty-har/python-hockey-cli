from models.positions import Position

def list_positions():
    positions = Position.get_all()
    for position in positions:
        print(position)

def exit_program():
    print("Goodbye!")
    exit()