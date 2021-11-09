import os
import sqlite3
import string

def connect():
    db_path = os.path.join(os.path.dirname(__file__), "example.db")
    if os.path.exists(db_path):
        return sqlite3.connect(db_path)
    else:
        con = sqlite3.connect(db_path)

        con.execute("CREATE TABLE letters (id int, letter text)")

        for i, l in enumerate(string.ascii_lowercase):
            con.execute("INSERT INTO letters VALUES (%d, '%s')" % (i+1, l))

        con.commit()

        return con
