import pytest
from starlette.testclient import TestClient
from main import app, books


client = TestClient(app)

INITIAL_BOOKS = {
    1: {"id": 1, "title": "Dune", "author": "Herbert", "year": 1900},
    2: {"id": 2, "title": "1984", "author": "Orwell", "year": 1921},
    3: {"id": 3, "title": "Brave New World", "author": "Huxley", "year": 1921},
}

@pytest.fixture(autouse=True)
def reset_books():
    books.clear()
    books.update(INITIAL_BOOKS)


def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200

    assert response.json()["title"] == "Dune"
    assert response.json()["author"] == "Herbert"
    assert response.json()["year"] == 1900

def test_get_book_not_found():
    response = client.get("/books/99")
    assert response.status_code == 404

def test_create_book():
    payload = {"title": "The Hobbit", "author": "Tolkien", "year": 1937}
    response = client.post("/books", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "Tolkien"
    assert data["year"] == 1937
