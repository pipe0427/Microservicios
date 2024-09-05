from fastapi import APIRouter, Body
from schemas.book_schema import Book

book_route = APIRouter()

@book_route.get("/")
def get_all_books():
    try:
        return "All books"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.get("/{bookId}")
def get_book(bookId: int):
    try:
        return bookId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.post("/")
def create_book(book: Book = Body(...)):
    try:
        return book
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.put("/")
def update_user(book: Book = Body(...)):
    try:
        return book
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.delete("/{bookId}")
def delete_user(bookId: int):
    try:
        return bookId
    except Exception as e:
        print(e)
        return {"error": str(e)}