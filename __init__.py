import sqlite3

CONN = sqlite3.connect("Bank.db")
CURSOR = CONN.cursor()


# CONN is a constant equal to a hash that contains a connection to the database.
# CURSOR is a constant that allows us to interact with the database and execute SQL statements
