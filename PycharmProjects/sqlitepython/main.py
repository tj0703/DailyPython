import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    # prerequisite: create folder /sqlite/db for db file creation
    # note : if path = :memory: the db file will be created in
    # the memory (RAM) instead of the folder on the disk
    create_connection(r"/Users/Tanvi/sqlite/db/pythonsqlite.db")