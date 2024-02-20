from fastapi import FastAPI, Header, Depends, APIRouter
from fastapi.responses import FileResponse

from models.models import Answer, Product, ListOfProducts, ProductAdd, User
from typing import Annotated

from repository import UserRepository

router = APIRouter(
    tags=["Юзвери"]
)
@router.get("/")
async def root():
    return FileResponse('static/index.html')


@router.post("/register")
async def register(user: Annotated[User, Depends()]):
    user_id = await UserRepository.add_user(user)
    return {'ok': True, 'user_id': user_id}

@router.post("/users")
async def get_users():
    users = await UserRepository.get_all()
    return {'users': users}
