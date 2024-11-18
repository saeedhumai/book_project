from fastapi import Body, FastAPI
import uvicorn
import httpx
import asyncio

app = FastAPI()
books = [
    {"title": "BookOne", "author": "Author One", "category": "math"},
    {"title": "BookTwo", "author": "Author Two", "category": "science"},
    {"title": "BookThree", "author": "Author Two", "category": "literature"},
    {"title": "BookFour", "author": "Author Four", "category": "math"},
    {"title": "BookFive", "author": "Author One", "category": "science"},
    {"title": "BookSix", "author": "Author Six", "category": "math"},
    {"title": "BookSeven", "author": "AuthorTwo", "category": "science"}
]

@app.get("/books/getbookbyauthor")
async def fetch_books(book_author: str):
    list_of_books = []
    for book in books:
        if book.get("author").casefold() == book_author.casefold():
            list_of_books.append(book)
    return list_of_books


@app.get("/books")
async def read_all_books():
    return books

@app.get("/books/query")
async def get_book_by_query(category: str):
    book_to_return = []
    for book in books:
        if book["category"].casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return

@app.get("/books/{book_author}")
async def get_books_author_and_category(book_author: str, category: str):
    book_to_return = []
    for book in books:
        if book["author"].casefold() == book_author.casefold() and book["category"].casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return

@app.post("/books/create")
async def create_book(book: dict = Body()):
    books.append(book)
    return book

@app.put("/books/update")
async def update_book(updated_book: dict = Body()):
    for i in range(len(books)):
        if books[i]["title"].casefold() == updated_book["title"].casefold():
            books[i] = updated_book
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}

@app.delete("/books/delete/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(books)):
        if books[i]["title"].casefold() == book_title.casefold():
            books.pop(i)
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}

async def test_apis():
    """Function to test all API endpoints"""
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        # Test GET all books
        response = await client.get("/books")
        print("All books:", response.json())

        # Test GET books by category
        response = await client.get("/books/query?category=math")
        print("Math books:", response.json())

        # Test POST new book
        new_book = {
            "title": "NewBook",
            "author": "New Author",
            "category": "fiction"
        }
        response = await client.post("/books/create", json=new_book)
        print("Created book:", response.json())

        # Test PUT update book
        update_book = {
            "title": "NewBook",
            "author": "Updated Author",
            "category": "non-fiction"
        }
        response = await client.put("/books/update", json=update_book)
        print("Update response:", response.json())

        # Test DELETE book
        response = await client.delete("/books/delete/NewBook")
        print("Delete response:", response.json())
