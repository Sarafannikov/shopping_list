from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.models import User, Auth
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

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


@app.post("/auth")
async def auth(logpas: Auth):
    logpas = dict(logpas)
    if logpas['login'] == '123' and logpas['password'] == '234':
        return True
    else:
        raise Exception('Неверный логин или пароль')
