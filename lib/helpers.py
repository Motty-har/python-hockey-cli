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

def update_position():#need help with this function
    id_ = input("Enter the position id: ")
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
    pass

def exit_program():
    print("Goodbye!")
    exit()