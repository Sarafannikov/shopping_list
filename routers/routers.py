import sqlalchemy
from fastapi import FastAPI, Header, Depends, APIRouter
from fastapi.responses import FileResponse

from models.models import Answer, Product, ListOfProducts, User
from typing import Annotated

from repository import UserRepository, ProductListRepository, ProductsRepository
import hashlib
import app.jwtClass


router = APIRouter()




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


@router.post("/auth")
async def login(user: Annotated[User, Depends()]):
    password = hashlib.sha256(user.password.encode()).hexdigest()
    check = await UserRepository.get_user(user.login)
    if check == []:
        return {'ok': False, 'message': 'Пользователь не найден'}
    if password == check.password:
        return {"access_token": app.jwtClass.create_jwt_token({"sub": user.login}), "token_type": "bearer"}
    return {'ok': False, 'message': 'Что то пошло не так'}




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
async def add_product_in_list(product: Annotated[Product, ''] = Depends(app.jwtClass.get_user_from_token)):
    product_id = await ProductsRepository.add_product(product)
    return {'product': product_id}

@router.post("/products_api")
async def get_products_from_list(id: int):
    product_id = await ProductsRepository.get_from_list(id)
    return {'product': product_id}


@router.get("/products/")
async def products(list_id):
    return FileResponse('static/products.html')


@router.post("/delete_poduct")
async def deleteProduct(id: int):
    product_id = await ProductsRepository.delete(id)
    return product_id


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


