from pydantic import BaseModel
from datetime import datetime
from typing import List


class User(BaseModel):
    login: str
    password: str


class Answer(BaseModel):
    status: str
    message: str


class Product(BaseModel):
    name: str
    quantity: int | float
    position: int


class ListOfProducts(BaseModel):
    products: List[Product]
