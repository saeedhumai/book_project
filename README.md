# Book API

This project is a FastAPI-based application that provides endpoints to manage a collection of books.

## Endpoints

### Get All Books

- **URL:** `/books/`
- **Method:** `GET`
- **Description:** Returns a list of all books.

### Get Books by Category

- **URL:** `/books/{category}`
- **Method:** `GET`
- **Description:** Returns a list of books that match the specified category.

### Get Book by Title

- **URL:** `/books/{dynamic_param}`
- **Method:** `GET`
- **Description:** Returns a book that matches the specified title.

### Update a Book

- **URL:** `/books/update_book/`
- **Method:** `PUT`
- **Description:** Updates an existing book in the collection.

## Running the Application

1. **Install dependencies:**
   ```sh
   pip install fastapi uvicorn
