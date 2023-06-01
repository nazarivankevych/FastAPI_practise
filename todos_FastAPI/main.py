"""
Authentication and authorization
- create endpoint
- make changes
- create a database for user
- validations
"""
from fastapi import FastAPI

import models
from database import engine
from routers import auth, todos, admin


app = FastAPI()
# Uncomment if need to create a new tables
# models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
