from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Book 1", "author": "Author 1"},
    {"title": "Book 2", "author": "Author 2"},
    {"title": "Book 3", "author": "Author 3"},
    {"title": "Book 4", "author": "Author 4"},
    {"title": "Book 5", "author": "Author 5"},
    {"title": "Book 6", "author": "Author 6"},
    {"title": "Book 7", "author": "Author 7"},
    {"title": "Book 8", "author": "Author 8"},
    {"title": "Book 9", "author": "Author 9"},
    {"title": "Book 10", "author": "Author 10"},
]

def get_all_books():
    return books



def get_book_by_title(book_title):
    new_books = []
    for book in books:
        if book_title.lower() == book["title"].lower():
            new_books.append(book)
    return new_books

@app.get("/")
def read_root():
    return {"Python is the best programming language!"}


@app.get("/all-books")
def all_books():
    response = get_all_books()
    return response


@app.post("/get-book-by-name")
def book_by_name(request:dict):
    book_name = request["book_name"]
    response = get_book_by_title(book_name)
    return response



#print(get_book_by_title("book 1"))