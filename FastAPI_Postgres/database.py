from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# link to database
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:xP809RC6!@localhost/TodoApplicationDatabase'
# make connection with sqlalchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create an auto commits to database
Base = declarative_base()
