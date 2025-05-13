# Import FastAPI framework to build the API
from fastapi import FastAPI
# Import BaseModel from pydantic for validating request data
from pydantic import BaseModel
# Regular expressions module, used later to extract numbers from book titles
import re
# Datetime module, for tracking borrow and return dates
from datetime import datetime


# Create Pydantic models for structured data validation in POST requests

class BookFullRequest(BaseModel):
    """Model used when full book details (title, author, id) are provided in a request."""
    book_name: str
    author_name: str
    book_id: int

    def __getitem__(self, item):  
        # Enables dictionary-style access (e.g. request["book_name"])
        return getattr(self, item)

class BookRequest(BaseModel):
    """Model used for general book data (title and author only)."""
    book_name: str
    author_name: str

    def __getitem__(self, item):
        return getattr(self, item)

class BookNameRequest(BaseModel):
    """Model used for requests where only the book name is needed."""
    book_name: str

    def __getitem__(self, item):
        return getattr(self, item)

class BookAuthorRequest(BaseModel):
    """Model used for requests where only the author's name is required."""
    author_name: str

    def __getitem__(self, item):
        return getattr(self, item)


# Sample in-memory book database with mock data
# Each book has an id, title, author, shelf status, and borrow count
# Some books include borrow_date to calculate overdue fines
books = [
    {"id": 101, "title": "The Pragmatic Programmer 1", "author": "Andrew Hunt", "in_shelf": True, "times_borrowed": 5},
    {"id": 203, "title": "Clean Code 4", "author": "Robert C. Martin", "in_shelf": False, "times_borrowed": 12, "borrow_date": datetime(2025, 4, 1)},
    {"id": 283, "title": "Introduction to Algorithms 5", "author": "Thomas H. Cormen", "in_shelf": True, "times_borrowed": 7},
    {"id": 428, "title": "Design Patterns 6", "author": "Erich Gamma", "in_shelf": True, "times_borrowed": 4},
    {"id": 285, "title": "Python Crash Course 2", "author": "Eric Matthes", "in_shelf": False, "times_borrowed": 8, "borrow_date": datetime(2025, 4, 15)},
    {"id": 628, "title": "Data Science from Scratch 7", "author": "Joel Grus", "in_shelf": True, "times_borrowed": 3},
    {"id": 773, "title": "You Don't Know JS 3", "author": "Kyle Simpson", "in_shelf": True, "times_borrowed": 6},
    {"id": 838, "title": "Deep Learning 9", "author": "Ian Goodfellow", "in_shelf": True, "times_borrowed": 2},
    {"id": 937, "title": "Fluent Python 8", "author": "Luciano Ramalho", "in_shelf": True, "times_borrowed": 12},
    {"id": 100, "title": "Effective Java 10", "author": "Joshua Bloch", "in_shelf": False, "times_borrowed": 9, "borrow_date": datetime(2025, 4, 25)},
]


# Utility function to retrieve all books
def get_all_books():
    return books


# Utility function to check if a number is prime
def is_prime(n):
    """Determine whether a given number is prime or not."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check divisibility from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Search for books by exact title (case-insensitive)
def get_book_by_title(book_title):
    new_books = []
    for book in books:
        if book_title.lower() == book["title"].lower():
            new_books.append(book)
    if not new_books:
        return "Book not Found"
    return new_books


# Function to calculate overdue fines
def pay_fine(present_book):
    """Compute fine if the book is overdue.
    First 14 days are free. Fine of 500 per extra day.
    """
    borrowing_limit = 14
    fine_rate = 500
    now = datetime.now()

    borrowed_date = present_book["borrow_date"]
    day_difference = abs((now - borrowed_date).days)

    if day_difference > borrowing_limit:
        fine = (day_difference - borrowing_limit) * fine_rate
    else:
        fine = 0

    return fine 


# Create FastAPI instance
app = FastAPI()


# Root endpoint to confirm server is running
@app.get("/")
def read_root():
    return {"Python is the best programming language!"}


# Endpoint to fetch all books
@app.get("/all-books")
def all_books():
    return get_all_books()


# Search book by title
@app.post("/get-book-by-name")
def book_by_name(request: BookNameRequest):
    book_name = request["book_name"]
    return get_book_by_title(book_name)


# Search books by author
@app.post("/get-books-by-author")
def book_by_author(request: BookAuthorRequest):
    author = request["author_name"]
    new_books = []
    for book in books:
        if author.lower() == book["author"].lower():
            new_books.append(book)
    if not new_books:
        return "Book not Found"
    return new_books


# Add a new book only if it doesn't already exist
@app.post("/add-book")
def add_book(request: BookFullRequest):
    book_id = request["book_id"]
    title = request["book_name"]
    author = request["author_name"]

    for book in books:
        if title.lower() == book["title"].lower() and author.lower() == book["author"].lower():
            return "Book already exists"
        
    books.append({"id": book_id, "title": title, "author": author, "in_shelf": True, "times_borrowed": 0})
    return {"reply": "New book added", "books": books}


# Return books whose title ends in a prime number (extracted using regex)
@app.get("/get-prime-suffix")
def get_books_with_prime_suffix():
    new_books = []
    for book in books:
        title = book["title"]
        match = re.search(r"\d+", title)  # Extract digits from the title
        if match:
            number = int(match.group())
            if is_prime(number):
                new_books.append(book)
    return new_books


# Delete a book by title
@app.post("/delete-by-name")
def delete_book_by_name(request: BookNameRequest):
    index = 0
    status = "Not found"
    title = request["book_name"]

    for book in books:
        if title.lower() == book["title"].lower():
            status = "Book Deleted"
            del books[index]
            break
        index += 1

    return {"status": status, "books": books}


# Borrow book using author's name
@app.post("/borrow-book-by-author")
def borrow_book_by_author(request: BookAuthorRequest):
    author = request["author_name"]
    status = "Book Not Found"
    for book in books:
        if author.lower() == book["author"].lower():
            if book["in_shelf"]:
                book["in_shelf"] = False
                book["borrow_date"] = datetime.now()
                book["times_borrowed"] += 1
                status = "Book has been borrowed"
            else:
                status = "Book not in shelf"
            break
    return status


# Borrow book using title
@app.post("/borrow-book-by-title")
def borrow_book_by_title(request: BookNameRequest):
    title = request["book_name"]
    status = "Book Not Found"
    for book in books:
        if title.lower() == book["title"].lower():
            if book["in_shelf"]:
                book["in_shelf"] = False
                book["borrow_date"] = datetime.now()
                book["times_borrowed"] += 1
                status = "Book has been borrowed"
            else:
                status = "Book not in shelf"
            break
    return status


# Return book by author name
@app.post("/return-book-by-author")
def return_book_by_author(request: BookAuthorRequest):
    author = request["author_name"]
    status = "Book Not Found"
    fine = 0

    for book in books:
        if author.lower() == book["author"].lower():
            if not book["in_shelf"]:
                book["in_shelf"] = True
                fine = pay_fine(book)
                status = "Book has been Returned"
            else:
                status = "Book already in shelf"
            break

    return {"fine": fine, "status": status}


# Return book by title
@app.post("/return-book-by-title")
def return_book_by_title(request: BookNameRequest):
    title = request["book_name"]
    status = "Book Not Found"
    fine = 0

    for book in books:
        if title.lower() == book["title"].lower():
            if not book["in_shelf"]:
                book["in_shelf"] = True
                fine = pay_fine(book)
                status = "Book has been Returned"
            else:
                status = "Book already in shelf"
            break

    return {"fine": fine, "status": status}


# List all currently borrowed books
@app.get("/get-borrowed-books")
def get_borrowed_books():
    return [book for book in books if not book["in_shelf"]]


# List all available books on the shelf
@app.get("/get-available-books")
def get_available_books():
    return [book for book in books if book["in_shelf"]]


# Return books that have been borrowed the most times
@app.get("/most-borrowed-book")
def most_borrowed_book():
    # First, find the maximum borrow count
    most_borrowed = max(books, key=lambda x: x["times_borrowed"])["times_borrowed"]
    # Return all books with that max count (in case of ties)
    return list(filter(lambda x: x["times_borrowed"] == most_borrowed, books))
