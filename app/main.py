from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from models.models import User, Answer, Product, ListOfProducts
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from peewee import *
import routers.create_db

app = FastAPI()

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

# Пример продуктового листа
#productOne = Product(name='Молоко', quantity=2, position=1)
#productTwo = Product(name='Хлеб', quantity=1, position=2)
#roductList = ListOfProducts(products=[productOne, productTwo])


@app.get("/")
async def root():
    return FileResponse('static/index.html')


@app.post("/auth", response_model=Answer)
async def auth(login, password: str):
    if login == '123' and password == '234':
        return {'status': 'ok', 'message': 'Вы успешно авторизованы'}
    else:
        return {'status': 'error', 'message': 'Неверный логин или пароль'}




#app.post('/list')
#async def get_product_list():
    #return productList
