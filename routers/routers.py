import sqlalchemy
from fastapi import FastAPI, Header, Depends, APIRouter
from fastapi.responses import FileResponse

from models.models import Answer, Product, ListOfProducts, User
from typing import Annotated

from repository import UserRepository, ProductListRepository, ProductsRepository
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
    try:
        user_id = await UserRepository.add_user(user)
    except sqlalchemy.exc.IntegrityError:
        return {'ok': False, 'message': "Данный логин уже занят"}
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


@router.post("/add_product_in_list")
async def add_product_in_list(product: Annotated[Product, Depends()]):
    product_id = await ProductsRepository.add_product(product)
    return {'product': product_id}

@router.post("/products_api")
async def get_products_from_list(id: int):
    product_id = await ProductsRepository.get_from_list(id)
    return {'product': product_id}


@router.get("/products")
async def root():
    return FileResponse('static/productlist.html')
