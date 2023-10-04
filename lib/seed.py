#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.positions import Position
from models.player import Player

def seed_database():
    Player.drop_table()
    Position.drop_table()
    Position.create_table()
    Position.create("Center", "Offense")
    Player.create_table()


seed_database()
print("Seeded database")
