from models.__init__ import CURSOR, CONN
from models.position import Position

class Player():
    
    all = {}
    
    def __init__(self, name, number, goals, assists, position_id, id=None):
        self.id = id
        self.name = name
        self.number = number
        self.goals = goals
        self.assists = assists
        self.position_id = position_id

    def __repr__(self):
        return (
            f"<Player {self.id}: Name: {self.name}, #{self.number}, Goals: {self.goals}, Assists: {self.assists}, " +
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
        if isinstance(number, int):
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
        if isinstance(goals, int):
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
        if isinstance(assists, int):
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
                "position_id must reference a position in the database")
    
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
    
    def save(self):
        """ Insert a new row with the name, number, goals, assists, and position id values of the current Player object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO players (name, number, goals, assists, position_id)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.number, self.goals, self.assists, self.position_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, number, goals, assists, position_id):
        """ Initialize a new Player instance and save the object to the database """
        player = cls(name, number, goals, assists, position_id)
        player.save()
        return player
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""

        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
            player.number = row[2]
            player.goals = row[3]
            player.assists = row[4]
            player.position_id = row[5]
        else:
            player = cls(row[1], row[2], row[3], row[4], row[5])
            player.id = row[0]
            cls.all[player.id] = player
        return player   
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Player object per table row"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_position_id(cls, id):
        """Return Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE position_id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def update(self):
        """Update the table row corresponding to the current Player instance."""
        sql = """
            UPDATE players
            SET name = ?, number = ?, goals = ?, assists = ?, position_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.number, self. goals, self.assists,
                             self.position_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current PLayer instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    def delete_by_position(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE position_id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    @classmethod
    def find_by_name(cls, name):
        """Return Player object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM players
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None