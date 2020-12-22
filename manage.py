import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'topsoft_db.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    connection = sqlite3.connect(db_path)
    return connection


from sqlalchemy.engine.url import URL
sqlite_db = {'drivername': 'sqlite', 'database': 'topsoft_db.sqlite3'}
print(URL(**sqlite_db))