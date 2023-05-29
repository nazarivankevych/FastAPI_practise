from fastapi import FastAPI
import logging

from validators import BookRequest

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)

app = FastAPI()


class Book:
    id: int
    title: int
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Computer Science Pro", 'codingwithnazar', 'A very nice book!', 5),
    Book(2, "Statistics Science Pro", 'codingwithnazar', 'A use fool book!', 5),
    Book(3, "Python for beginners", 'codingwithnazar', 'Nice book to start coding on Python!', 5),
    Book(4, "Math for scientist", 'codingwithnazar', 'Science in Python', 1),
    Book(5, "Use this modules for automation", 'codingwithnazar', 'Automate routine tasks with Python', 2),
    Book(6, "Test with Python", 'codingwithnazar', 'Automate routine tasks with Python', 3)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    # logging.info(type(new_book))
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book
