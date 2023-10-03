from models.__init__ import CURSOR, CONN

class Position():
    
    all = {}

    def __init__(self, position, type, id = None):
        self.id = id
        self.position = position
        self.type = type

    def __repr__(self):
        return f"<{self.id}: Pos: {self.position}, Type: {self.type}>"
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, str) and len(position):
            self._position = position
        else:
            raise ValueError(
                "Position must be a non-empty string"
            )

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str) and len(type):
            self._type = type
        else:
            raise ValueError(
                "Type must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Position instances """
        sql = """
            CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY,
            position TEXT,
            type Text)
        """
        CURSOR.execute(sql)
        CONN.commit()
