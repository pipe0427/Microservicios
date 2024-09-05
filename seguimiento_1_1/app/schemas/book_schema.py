from pydantic import BaseModel

class Book(BaseModel):
    tittle: str
    author: str
    age: int
    category: str
    isbn: int
