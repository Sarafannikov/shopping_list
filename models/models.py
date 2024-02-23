from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class User(BaseModel):
    login: str
    password: str


class Answer(BaseModel):
    status: str
    message: str


class Product(BaseModel):
    id: int
    name: str
    quantity: Optional[float] = None  # Optional - не обязательное поле
    position: int


class ListOfProducts(BaseModel):
    id: int
    user_id: int
