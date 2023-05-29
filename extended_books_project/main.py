from fastapi import FastAPI, Path, Query, HTTPException
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
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


BOOKS = [
    Book(1, "Computer Science Pro", 'codingwithnazar', 'A very nice book!', 5, 2005),
    Book(2, "Statistics Science Pro", 'codingwithnazar', 'A use fool book!', 5, 2007),
    Book(3, "Python for beginners", 'codingwithnazar', 'Nice book to start coding on Python!', 5, 2010),
    Book(4, "Math for scientist", 'codingwithnazar', 'Science in Python', 1, 2012),
    Book(5, "Use this modules for automation", 'codingwithnazar', 'Automate routine tasks with Python', 2, 2012),
    Book(6, "Test with Python", 'codingwithnazar', 'Automate routine tasks with Python', 3, 2012)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/published_date/")
async def get_book_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


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


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')