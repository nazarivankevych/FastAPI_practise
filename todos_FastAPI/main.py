"""
Add, remove, change, make prioritizations of todos.
- create todos
- make changes
- delete todos
- mark them
- create a database for todos
- validations
"""
from typing import Annotated
from sqlalchemy.orm import Session

from fastapi import FastAPI, HTTPException, Depends
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal


app = FastAPI()
# Use if you do not have DB
# models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except ConnectionError as e:
        print(f"Ups, something went wrong: {e}")
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()
