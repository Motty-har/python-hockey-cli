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

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if isinstance(number, int) and len(number):
            self._number = number
        else:
            raise ValueError(
                "Number must be a number"
            )
    
    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self, goals):
        if isinstance(goals, int) and len(goals):
            self._goals = goals
        else:
            raise ValueError(
                "Goals must be a number"
            )
    
    @property
    def assists(self):
        return self._assists
    
    @assists.setter
    def assists(self, assists):
        if isinstance(assists, int) and len(assists):
            self._assists = assists
        else:
            raise ValueError(
                "Assists must be a number"
            )
    
    @property
    def position_id(self):
        return self._position_id
    
    @position_id.setter
    def position_id(self, position_id):
        if type(position_id) is int and Position.find_by_id(position_id):
            self._position_id = position_id
        else:
            raise ValueError(
                "position_id must reference a department in the database")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Player instances """
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            number INTEGER,
            goals INTEGER,
            assists INTEGER,
            position_id INTEGER,
            FOREIGN KEY (position_id) REFERENCES positions(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Player instances """
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()