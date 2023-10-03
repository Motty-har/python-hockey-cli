from models.__init__ import CURSOR, CONN

class Position():
    
    all = {}

    def __init__(self, position, type, id = None):
        self.id = id
        self.position = position
        self.type = type

    def __repr__(self):
        return f"<{self.id}: Pos: {self.position}, Type: {self.type}>"
    
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
