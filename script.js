const bookForm = document.getElementById('bookForm');
const bookList = document.getElementById('bookList');

function loadBooks() {
  fetch('/books')
    .then(res => res.json())
    .then(books => {
      bookList.innerHTML = '';
      books.forEach(book => {
        const li = document.createElement('li');
        li.innerHTML = `
          <strong>${book.title}</strong> by ${book.author} - $${book.price} 
          [${book.genre}, Qty: ${book.quantity}]<br>ISBN: ${book.isbn}
          <div class="actions">
            <button class="edit" onclick="editBook(${book.id})">Edit</button>
            <button onclick="deleteBook(${book.id})">Delete</button>
          </div>
        `;
        bookList.appendChild(li);
      });
    });
}

bookForm.onsubmit = function (e) {
  e.preventDefault();
  const bookId = document.getElementById('bookId').value;
  const book = {
    title: document.getElementById('title').value,
    author: document.getElementById('author').value,
    genre: document.getElementById('genre').value,
    price: parseFloat(document.getElementById('price').value),
    quantity: parseInt(document.getElementById('quantity').value),
    isbn: document.getElementById('isbn').value
  };
