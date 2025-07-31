# Programming-for-Information-Systems---Project
Company Name : **The Bookhive**

Description:
The key reasons for selecting "The Bookhive" as the specific organization for this Information System are:

Clear Core Business: A bookstore, has a very tangible and easily definable core business: managing books, sales, and potentially customer interactions. 

Identifiable Data Entities: The primary data entity is "Book," which has straightforward attributes (Title, Author, ISBN, Stock). This simplicity allows for a clear focus on CRUD operations without getting bogged down in complex data relationships for a proof-of-concept.

Direct Operational Benefits: Even a basic system can significantly improve efficiency for a small bookstore by:
->Accurate Inventory: Knowing exactly what books are in stock and where.
->Faster Sales/Lookup: Quickly finding books for customers.
->Reduced Manual Errors: Automating data entry and updates reduces mistakes common with paper-based systems.
->Better Stock Management: Identifying low stock levels to reorder.

Scalability Potential: While this PoC focuses on books, the system could easily be extended in a full implementation to include:
Cafe inventory and sales.
Customer loyalty programs.
Staff management.

Implementaion :

**Bookstore Information System**

A simple full-stack Bookstore Management Web App built with Flask (Python) for the backend and HTML/CSS/JavaScript for the frontend. It allows users to add, view, edit, delete, and search book records, with persistent storage in a JSON file.

**-> Features**
Add new books with title, author, genre, price, quantity, and ISBN

Update and delete existing books

Search books by title or author (client-side filter)

Simple and clean UI with styled form and book display cards

RESTful API built using Flask

JSON-based data storage

Fully tested with pytest


**Requirements**

- Python 3.8+
- Flask
- Flask-CORS


**programming-for-information-system/**
│
├── app.py                # Backend 
├── books.json            # storage (JSON format)
├── testing.py            # Pytest unit tests
│
├── templates/
│   └── index.html        # Frontend 
│
├── static/
│   ├── script.js         # JavaScript logic
│   └── styles.css        # Styling for the app
│
└── README.md             # Documentation

**API Documentation**
Use Base URL with: /
Method	    Endpoint	          Description
GET	        /books	            Fetch all books
POST	      /books	            Add a new book
PUT	        /books/<int:id>	    Update a book by ID
DELETE	    /books/<int:id>	    Delete a book by ID

**Project Evolution**
The development of this Information System has followed an iterative process, starting with frontend scaffolding and gradually integrating backend capabilities. The commits reflect a strong focus on refining core functionalities, enhancing the user interface, and introducing testing procedures.

**Initial Setup & Frontend Foundation:**

Initial commit on May 21 marked the project's beginning.

The core frontend structure was laid out with the creation of index.html and initial styles.css.

Client-side interactivity began with the creation and initial updates of script.js.

An early data storage approach was explored with books.json, suggesting an initial flat-file, in-memory or local storage concept for data.

**Backend Integration & Core Functionality:**

Introduction of the Python Flask backend, marked by the creation and initial development of app.py to make the project a client-server architecture with persistent storage.

Subsequent updates to app.py and script.js (Jul 12) indicate the integration efforts between the new Flask backend and the JavaScript frontend.

**Refinement, CRUD Completion, UI Enhancements & Testing:**

Backend Structure: Adding the missing main method ensured the Flask application was properly runnable.

Database Operations: Adding update books and delete book methods for Completing CRUD operation solidified the full CRUD capabilities for the book entity.

**Frontend Structure & Styling:**

Update index.html and Setting Font,Background,Buttons, Border and Margins indicate initial styling efforts.

linking javascript file confirms the separation of JavaScript into script.js for better code organization.

Adding Search Bar and grid Book section, Styling the Book Grid, and Updating Book card and including filter function for SearchBox to enhance the book display, search, and filtering capabilities.

**Quality Assurance & Testing:**

Correcting Minor type errors and type errors reflect ongoing bug fixing and code refinement.

Book Details suggests a focus on the data integrity and display of book information.

The introduction of a dedicated testing file, Create testing.py, marks a crucial step towards formalizing the testing process. This was followed by tests,I took help from AI because lack of knowledge in testing which indicates the implementation of tests, with assistance sought due to a learning curve in this area.

**References:**
To Implement RESTful API i have taken Help of Chatgpt : https://chatgpt.com/c/688b5225-e7bc-8332-94bb-a5b412e08dba
To Create Book-Card with Crud Operation and Add Search Bar i have taken reference from ChatGpt : https://chatgpt.com/c/688b53ff-a34c-832b-9656-b2109d42afa6
I have gone through the Youtube tutorial Video : https://www.youtube.com/watch?v=3mLo0foh1LA&list=PLnkHcDuPoB7XFqRMo8t6V7PpJfCcyS4ir
The Folder Structure in the Readme file above is generated by Chatgpt.

**Google Maps Link of the Company :** The Book Hive,53 London Street, Norwich, NR2 1HL
