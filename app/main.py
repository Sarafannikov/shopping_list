from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.models import User, Answer, Product, ListOfProducts
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

# Пример продуктового листа
productOne = Product(name='Молоко', quantity=2, position=1)
productTwo = Product(name='Хлеб', quantity=1, position=2)
productList = ListOfProducts(products=[productOne, productTwo])

@app.get("/")
async def root():
    return FileResponse('static/index.html')


@app.post("/calc/")
async def calc(num1, num2):
    return {"result": sum([int(num1), int(num2)])}


@app.post("/user")
def get_user(user: User):
    res = dict(user)
    if res['age'] > 18:
        res['is_adult '] = True
    else:
        res['is_adult '] = False

    return res


@app.post("/auth/", response_model=Answer)
async def auth(login, password: str):
    if login == '123' and password == '234':
        return {'status': 'ok', 'message': 'Вы успешно авторизованы'}
    else:
        return {'status': 'error', 'message': 'Неверный логин или пароль'}


@app.post('/list')
async def get_product_list():
    return productList
