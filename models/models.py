from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Auth(BaseModel):
    login: str
    password: str
