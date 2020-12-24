from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

sqlite_db = {'drivername': 'sqlite', 'database': 'topsoft_db.sqlite3'}
engine = create_engine(URL(**sqlite_db))

Session = sessionmaker(bind=engine)
session = Session()
