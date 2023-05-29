from fastapi import FastAPI, Body

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
async def create_book(book_request=Body()):
    BOOKS.append(book_request)