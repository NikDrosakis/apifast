from typing import Union
from pydantic import BaseModel
class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

class BookCreate(BaseModel):
    title: str
    author: str

class Book(BookCreate):
    id: int