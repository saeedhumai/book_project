from fastapi import Body, FastAPI

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

@app.get("/books/")
async def read_all_book():
   return books


@app.get("books/")
async def get_book_by_query(category:str):
   book_to_return = []
   for book in books:
      if book.get["catagory"].casefold() == category.casefold():
         book_to_return.append(book)
   return book_to_return



 
@app.get("/books/{book_author}/")
async def get_books_auther_and_catagory(book_author: str ,catagory:str):
   book_to_return = []
   for book in books: 
      if book.get["author"].casefold()==book_author.casefold() and book.get["catagory"].casefold() == catagory.casefold():
         book_to_return.append(book)
   return book_to_return

@app.post("/books/create_book")
async def create_book(book=Body()):
   books.append(book)
   return book


@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
   for i in range(len(books)):
      if books[i].get("title").casefold() == updated_book.get("title").casefold():
         books[i] = updated_book
         return {"message": "Book updated successfully"}
   return {"error": "Book not found"}




@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str ):
   for i in range (len(books)):
      if books[i].get("title").casefold() == book_title.casefold():
         books.pop(i) 
         return {"message": "Book deleted successfully"}
   return {"error": "Book not found"}


# if __name__ == "__main__":