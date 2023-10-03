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
    def drop_table(cls):
        """ Drop the table that persists Position instances """
        sql = """
            DROP TABLE IF EXISTS positions;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
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
        

    def save(self):
        """ Insert a new row with the position and type values of the current Positions instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO positions (position, type)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.position, self.type))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, position, type):
        """ Initialize a new Position instance and save the object to the database """
        pos = cls(position, type)
        pos.save()
        return pos
    
