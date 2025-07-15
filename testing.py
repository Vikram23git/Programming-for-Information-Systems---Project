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

