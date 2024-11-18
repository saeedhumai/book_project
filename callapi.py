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
    {"title": "BookSeven", "author": "Author Two", "category": "science"}
]

# Your existing endpoints...

async def call_book_endpoints():
    async with httpx.AsyncClient() as client:
        # Call your own API endpoints
        base_url = "http://127.0.0.1:8000"
        
        # Example calls to your endpoints
        all_books = await client.get(f"{base_url}/books/")
        math_books = await client.get(f"{base_url}/books/?category=math")
        author_books = await client.get(f"{base_url}/books/Author One/?category=science")
        
        # Create a new book
        new_book = {
            "title": "NewBook",
            "author": "New Author",
            "category": "fiction"
        }
        created_book = await client.post(f"{base_url}/books/create_book", json=new_book)
        
        return {
            "all_books": all_books.json() if all_books.status_code == 200 else None,
            "math_books": math_books.json() if math_books.status_code == 200 else None,
            "author_books": author_books.json() if author_books.status_code == 200 else None,
            "created_book": created_book.json() if created_book.status_code == 200 else None
        }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # To test API calls, you would need to run this in a separate script after starting the server