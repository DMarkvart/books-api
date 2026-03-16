from fastapi import FastAPI, HTTPException, status
from schemas.book import BookCreate, BookResponse

app = FastAPI()

books = {
    1: {"id": 1, "title": "Dune", "author": "Herbert", "year": 1900},
    2: {"id": 2, "title": "1984", "author": "Orwell", "year": 1921},
    3: {"id": 3, "title": "Brave New World", "author": "Huxley", "year": 1921},
}


@app.get("/about")
def get_about() -> dict:
    return {
        "author": "Dima",
        "project": "books-api"
    }


@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=BookResponse)
def create_book(value: BookCreate) -> dict:
    book_id = max(books.keys()) + 1
    book = {"id": book_id, **value.model_dump()}
    books[book_id] = book
    return book


@app.get("/books")
def get_books(author: str | None = None, year: int | None = None) -> list[dict]:
    result = list(books.values())
    if author is not None:
        result = [book for book in result if book["author"] == author]
    if year is not None:
        result = [book for book in result if book["year"] == year]

    return result


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int)->BookResponse:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found by id")
    book = books[book_id]
    return book


@app.put("/books/{book_id}", response_model=BookResponse)
def update(book_id: int, payload: BookCreate):
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found by id")

    book = {"id": book_id, **payload.model_dump()}

    books[book_id] = book

    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(book_id: int) -> None:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found by id")
    del books[book_id]

    return None
