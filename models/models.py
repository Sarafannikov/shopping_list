from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class User(BaseModel):
    login: str
    password: str


class Answer(BaseModel):
    status: str
    message: str


class ProductAdd(BaseModel):
    name: str
    quantity: Optional[float] = None  # Optional - не обязательное поле
    position: int


class Product(ProductAdd):
    id: int


class ListOfProducts(BaseModel):
    products: List[Product]
