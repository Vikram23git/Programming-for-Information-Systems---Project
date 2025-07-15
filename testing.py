import pytest
from app import app, Books_File
import json
import os

@pytest.fixture
def client():
  if os.path.exists(Books_File):
    os.rename(Books_File, Books_File + ".bak")

  with open(Books_File, 'w') as f:
    json.dump([], f)
  
  with app.test_client() as client:
    yield client

  if os.path.exists(Books_File):
    os.remove(Books_File)
  if os.path.exists(Books_File + ".bak"):
    os.rename(Books_File + ".bak",Books_File)

def test_add_book(client):
  new_book = {
    "title": "Test Book",
    "author": "Tester",
    "genre": "Testing",
    "price": 10.0,
    "quantity": 5,
    "isbn": "0000001111"
  }
  response = client.post('/books', json=new_book)
  assert response.status_code == 200
  assert b'Book Added Successfully' in response.data

def test_get_books(client):
    # Add one book
    client.post('/books', json={
        "title": "Another Book",
        "author": "Someone",
        "genre": "Fiction",
        "price": 15.0,
        "quantity": 3,
        "isbn": "1234567890"
    })

    response = client.get('/books')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['title'] == "Another Book"

def test_update_book(client):
    # Add a book
    client.post('/books', json={
        "title": "To Update",
        "author": "A",
        "genre": "Drama",
        "price": 20,
        "quantity": 2,
        "isbn": "111111"
    })
    response = client.put('/books/1', json={"title": "Updated Title"})
    assert response.status_code == 200
    assert b'updated' in response.data

def test_delete_book(client):
    # Add a book
    client.post('/books', json={
        "title": "To Delete",
        "author": "B",
        "genre": "Horror",
        "price": 18,
        "quantity": 1,
        "isbn": "999999"
    })
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert b'Deleted' in response.data
