#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.positions import Position

def seed_database():
    Position.create_table


seed_database()
print("Seeded database")
