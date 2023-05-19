from fastapi import FastAPI
from fastapi import Body

from constants import BOOKS

app = FastAPI()


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/{book_title}")
# async def read_books(book_title: str):
#     for book in BOOKS:
#         if book.get("title").casefold() == book_title.casefold():
#             return book


# @app.get("/books/")
# async def read_category_by_query(category: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get("category").casefold() == category.casefold():
#             books_to_return.append(book)
#     return books_to_return


@app.get("/books/{book_to_return}/")
async def read_author_category_by_query(book_title: str, book_author: str, book_category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold() or \
            book.get('author').casefold() == book_author.casefold() or \
                book.get('category').casefold() == book_category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
