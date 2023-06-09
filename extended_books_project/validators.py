from pydantic import BaseModel, Field
from typing import Optional


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: float = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'codingwithnazar',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2010
            }
        }
