from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Starter Data
books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English"
    },
    {
        "id": 2,
        "title": "Wings of Fire",
        "author": "A P J Abdul Kalam",
        "genre": "Biography",
        "language": "English"
    }
]


# Request Body Model
class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str


# Home Route
@app.get("/")
def home():
    return {
        "message": "Library API is running"
    }


# Get All Books
@app.get("/books")
def get_books():
    return books


# Add a New Book
@app.post("/books", status_code=201)
def create_book(book: BookCreate):

    # Generate a new ID
    new_id = max((b["id"] for b in books), default=0) + 1

    # Create the new book
    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "language": book.language
    }

    # Store it
    books.append(new_book)

    # Return success response
    return {
        "message": "Book added successfully",
        "book": new_book
    }