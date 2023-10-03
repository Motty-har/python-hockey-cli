from models.__init__ import CURSOR, CONN

class Position():
    
    all = {}

    def __init__(self, position, id = None):
        self.id = id
        self.position = position
        
