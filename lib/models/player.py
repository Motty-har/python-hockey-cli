from models.__init__ import CURSOR, CONN
from models.positions import Position

class Player():
    def __init__(self, name, number, goals, assists, position_id, id=None):
        self.id = id
        self.name = name
        self.number = number
        self.goals = goals
        self.assists = assists
        self.position_id = position_id

    def __repr__(self):
        return (
            f"<Employee {self.id}: Name: {self.name}, #: {self.number}, Goals: {self.goals}, Assists: {self.assists} " +
            f"Position ID: {self.position_id}>"
        )
