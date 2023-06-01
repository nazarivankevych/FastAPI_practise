from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# link to database
SQLALCHEMY_DATABASE_URL = 'sqlite:///tables/todoapp.db'
# make connection with sqlalchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
# create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create an auto commits to database
Base = declarative_base()
