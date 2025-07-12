from flask import Flask,jsonify,request,render_template
import json
from flask_cors import CORS

app = Flask (_name_)
CORS(app)

Books_File = 'books.json'

def read_books():
  try:
    with OPEN(Books_File,'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def write_books():
  with OPEN(Books_File, 'w') as file:
    return json.dump(data, file, indent=2)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/books',method=['GET'])
def get_books():
  return jsonify(read_books())

@app.route('/books',method=['POST'])
def add_books():
  books = read_books()
  new_book = request.json
  new_book['id'] = books[-1]['id'] + 1 if books else 1
  books.append(new_book)
  write_books(books)
  return jsonify({'Text Msg : Book Added Successfully'})
