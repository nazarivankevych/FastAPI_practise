from fastapi import FastAPI

from constants import BOOKS

app = FastAPI()

@app.get("/books")
async def read_all_books():
    return BOOKS