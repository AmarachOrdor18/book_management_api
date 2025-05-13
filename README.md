# Book Management API

This is a simple Book Management API built using FastAPI. It allows users to view, add, borrow, return, and delete books, as well as perform searches by title or author. It also calculates fines for late returns.

## Features

- Add new books
- View all books
- Search books by title or author
- Borrow and return books
- View available or borrowed books
- Get books with prime number suffix in titles
- See the most borrowed book
- Calculate late return fines

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/book-api.git
cd book-api
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the API server:

```bash
uvicorn assignment_2:app --reload
```


## How to Use the API

You can test this API using tools like Postman, curl, or directly from the FastAPI interactive docs at:

http://127.0.0.1:8000/docs

### 1. View All Books

- **Endpoint:** `GET /all-books`
- **Use case:** You want to see the list of every book in the library.

### 2. Add a New Book

- **Endpoint:** `POST /add-book`
- **Body Example:**

```json
{
  "book_name": "My New Book",
  "author_name": "Jane Doe",
  "book_id": 999
}
```

### 3. Find a Book by Title

- **Endpoint:** `POST /get-book-by-name`
- **Body Example:**

```json
{
  "book_name": "Clean Code 4"
}
```

### 4. Find a Book by Author

- **Endpoint:** `POST /get-books-by-author`
- **Body Example:**

```json
{
  "author_name": "Robert C. Martin"
}
```

### 5. Borrow a Book

#### By Title:

- **Endpoint:** `POST /borrow-book-by-title`
- **Body:**

```json
{
  "book_name": "Clean Code 4"
}
```

#### By Author:

- **Endpoint:** `POST /borrow-book-by-author`
- **Body:**

```json
{
  "author_name": "Robert C. Martin"
}
```

### 6. Return a Book (and Calculate Fine)

#### By Title:

- **Endpoint:** `POST /return-book-by-title`
- **Body:**

```json
{
  "book_name": "Clean Code 4"
}
```

#### By Author:

- **Endpoint:** `POST /return-book-by-author`
- **Body:**

```json
{
  "author_name": "Robert C. Martin"
}
```

### 7. Delete a Book

- **Endpoint:** `POST /delete-by-name`
- **Body:**

```json
{
  "book_name": "Old Book Title"
}
```

### 8. Get Borrowed Books

- **Endpoint:** `GET /get-borrowed-books`

### 9. Get Available Books

- **Endpoint:** `GET /get-available-books`

### 10. Get Books with Prime Number in Title

- **Endpoint:** `GET /get-prime-suffix`

### 11. Most Borrowed Book

- **Endpoint:** `GET /most-borrowed-book`

## Example Thought Scenarios

- **Librarian Jane** wants to add a new book when a shipment arrives. She uses the `/add-book` endpoint.
- **Student Mark** is looking for a specific title. He checks with `/get-book-by-name`.
- **User Amina** wants to borrow a book by her favorite author. She tries `/borrow-book-by-author`.
- **Library assistant Tolu** checks which books are overdue and need to be returned. They use `/get-borrowed-books`.
- **Admin James** reviews the most popular books by calling `/most-borrowed-book`.# Book Management API

This is a simple Book Management API built using FastAPI. It allows users to view, add, borrow, return, and delete books, as well as perform searches by title or author. It also calculates fines for late returns.

## Features

- Add new books
- View all books
- Search books by title or author
- Borrow and return books
- View available or borrowed books
- Get books with prime number suffix in titles
- See the most borrowed book
- Calculate late return fines

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AmarachOrdor18/book_management_api.git
cd book-api
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the API server:

```bash
uvicorn main:app --reload
```

Replace `main` with the name of your Python file if different.

## Requirements File Example (`requirements.txt`)

```txt
fastapi
uvicorn
pydantic
```

---

## How to Use the API

You can test this API using tools like Postman, curl, or directly from the FastAPI interactive docs at:

http://127.0.0.1:8000/docs

### 1. View All Books

- **Endpoint:** `GET /all-books`
- **Use case:** You want to see the list of every book in the library.

### 2. Add a New Book

- **Endpoint:** `POST /add-book`
- **Body Example:**

```json
{
  "book_name": "My New Book",
  "author_name": "Jane Doe",
  "book_id": 999
}
```

### 3. Find a Book by Title

- **Endpoint:** `POST /get-book-by-name`
- **Body Example:**

```json
{
  "book_name": "Clean Code 4"
}
```

### 4. Find a Book by Author

- **Endpoint:** `POST /get-books-by-author`
- **Body Example:**

```json
{
  "author_name": "Robert C. Martin"
}
```

### 5. Borrow a Book

#### By Title:

- **Endpoint:** `POST /borrow-book-by-title`
- **Body:**

```json
{
  "book_name": "Clean Code 4"
}
```

#### By Author:

- **Endpoint:** `POST /borrow-book-by-author`
- **Body:**

```json
{
  "author_name": "Robert C. Martin"
}
```

### 6. Return a Book (and Calculate Fine)

#### By Title:

- **Endpoint:** `POST /return-book-by-title`
- **Body:**

```json
{
  "book_name": "Clean Code 4"
}
```

#### By Author:

- **Endpoint:** `POST /return-book-by-author`
- **Body:**

```json
{
  "author_name": "Robert C. Martin"
}
```

### 7. Delete a Book

- **Endpoint:** `POST /delete-by-name`
- **Body:**

```json
{
  "book_name": "Old Book Title"
}
```

### 8. Get Borrowed Books

- **Endpoint:** `GET /get-borrowed-books`

### 9. Get Available Books

- **Endpoint:** `GET /get-available-books`

### 10. Get Books with Prime Number in Title

- **Endpoint:** `GET /get-prime-suffix`

### 11. Most Borrowed Book

- **Endpoint:** `GET /most-borrowed-book`

## Example Thought Scenarios

- **Librarian Jane** wants to add a new book when a shipment arrives. She uses the `/add-book` endpoint.
- **Student Mark** is looking for a specific title. He checks with `/get-book-by-name`.
- **User Amina** wants to borrow a book by her favorite author. She tries `/borrow-book-by-author`.
- **Library assistant Tolu** checks which books are overdue and need to be returned. They use `/get-borrowed-books`.
- **Admin James** reviews the most popular books by calling `/most-borrowed-book`.