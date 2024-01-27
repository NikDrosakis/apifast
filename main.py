from fastapi import FastAPI
from models import Item, BookCreate, Book
import sqlite3
def create_connection():
 connection = sqlite3.connect("books.db")
 return connection
def create_table():
 connection = create_connection()
 cursor = connection.cursor()
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS books (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 author TEXT NOT NULL
 )
 """)
 connection.commit()
 connection.close()

create_table() # Call this function to create the table

def create_book(book: BookCreate):
 connection = create_connection()
 cursor = connection.cursor()
 cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book.title, book.author))
 connection.commit()
 connection.close()
from typing_extensions import Annotated
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/items/")
async def getallitems():
    return {"message":"all items"}
@app.get("/items/{id}")
async def getoneitem(id):
    return {"message":"item "+ id}

@app.post("/items/")
async def create_item(item: Item):
    return item
@app.post("/books/")
def create_book_endpoint(book: BookCreate):
 book_id = create_book(book)
 return {"id": book_id, **book.dict()}