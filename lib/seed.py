#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.position import Position
from models.player import Player

def seed_database():
    Player.drop_table()
    Position.drop_table()
    Position.create_table()
    Position.create("Lefr Wing", "Offense")
    Position.create("Left Defense", "Defense")
    Player.create_table()
    Player.create("Artemi Panarin", 10, 31, 92, 1)
    Player.create("Adam Fox", 23, 22, 84, 2)


seed_database()
print("Seeded database")
