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
