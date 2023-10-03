from models.__init__ import CURSOR, CONN

class Position():
    
    all = {}

    def __init__(self, position, type, id = None):
        self.id = id
        self.position = position
        self.type = type

    def __repr__(self):
        return f"<{self.id}: Position: {self.position}, Type: {self.type}>"
    
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
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Position object having the attribute values from the table row."""

        pos = cls.all.get(row[0])
        if pos:
            pos.position = row[1]
            pos.type = row[2]
        else:
            pos = cls(row[1], row[2])
            pos.id = row[0]
            cls.all[pos.id] = pos
        return pos

    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM positions
        """

        rows = CURSOR.execute(sql).fetchall()
        all_rows = [cls.instance_from_db(row) for row in rows] 
        return all_rows
    
