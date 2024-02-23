from fastapi import FastAPI, Header, Depends, APIRouter
from fastapi.responses import FileResponse

from models.models import Answer, Product, ListOfProducts, User
from typing import Annotated

from repository import UserRepository, ProductListRepository
import hashlib

router = APIRouter(
    tags=["Апишечка"]
)
@router.get("/")
async def root():
    return FileResponse('static/index.html')


@router.post("/register")
async def register(user: Annotated[User, Depends()]):
    user.password = hashlib.sha256(user.password.encode()).hexdigest()
    user_id = await UserRepository.add_user(user)
    return {'ok': True, 'user_id': user_id}

@router.post("/users")
async def get_users():
    users = await UserRepository.get_all()
    return {'users': users}


@router.post("/product_list")
async def get_productlist():
    productlist = await ProductListRepository.get_all()
    return {'productlist': productlist}

@router.post("/add_productlist")
async def add_productlist(productlist: Annotated[ListOfProducts, Depends()]):
    productlist_id = await ProductListRepository.add_productlist(productlist)
    return {'productlist_id': productlist_id}
