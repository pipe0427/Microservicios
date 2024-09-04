from fastapi import APIRouter, Body
from models.book_schema import Book

from database import BookModel

book_route = APIRouter()

@book_route.get("/")
def get_all_books():
    try:
        books = list(BookModel.select())
        return books
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.get("/{bookId}")
def get_book(bookId: int):
    try:
        book = BookModel.get(BookModel.id == bookId)
        return book
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.post("/")
def create_book(book: Book = Body(...)):
    try:
        BookModel.create(tittle=book.tittle, author=book.author, age=book.age,category=book.category, isbn=book.isbn)
        return pc
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.put("/")
def update_user(bookId: int,book: Book = Body(...)):
    try:
        existing_book = BookModel.get(BookModel.id == bookId)

        if existing_book is None:
            return "The book doesnt exist"
        else:
            existing_book.tittle = book.tittle
            existing_book.author = book.author
            existing_book.age = book.age
            existing_book.category = book.category
            existing_book.isbn = book.isbn

            existing_book.save()
            return "Book updated successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.delete("/{bookId}")
def delete_user(bookId: int):
    try:
        book = BookModel.get(BookModel.id == bookId)
        if book is None:
            return "The book doesnt exist"
        else: 
            book.delete_instance()
            return "Book delete successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}