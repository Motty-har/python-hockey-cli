import sqlite3

CONN = sqlite3.connect("roster_tracker.db")
CURSOR = CONN.cursor()
