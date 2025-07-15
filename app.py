from flask import Flask,jsonify,request,render_template
import json
from flask_cors import CORS

app = Flask (__name__)
CORS(app)

Books_File = 'books.json'

def read_books():
  try:
    with open(Books_File,'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def write_books(data):
  with open(Books_File, 'w') as file:
    return json.dump(data, file, indent=2)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/books',methods=['GET'])
def get_books():
  return jsonify(read_books())

@app.route('/books',methods=['POST'])
def add_books():
  books = read_books()
  new_book = request.json
  new_book['id'] = books[-1]['id'] + 1 if books else 1
  books.append(new_book)
  write_books(books)
  return jsonify({'Text Msg' : 'Book Added Successfully'})

@app.route('/books/<int:book_id>',methods=['PUT'])
def update_books(book_id):
  books = read_books()
  for book in books:
    if book['id'] == book_id:
      updated = request.json
      book.update(updated)
      write_books(books)
      return jsonify({'msg': 'Book has been updated'})
    return jsonify({'error':'Book not found'}),404

@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
  books = read_books()
  books = [book for book in books if book['id'] != book_id]
  write_books(books)
  return jsonify({'msg':'Book Deleted'})

if __name__ =='__main__':
  app.run(debug=True)
