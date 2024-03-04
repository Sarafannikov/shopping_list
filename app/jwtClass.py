import jwt
from env import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPBearer
from fastapi import Depends

http_bearer = HTTPBearer()


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)  # кодируем токен, передавая в него наш словарь с тем, что мы хотим там разместить


# Функция получения User'а по токену
async def get_user_from_token(token: str = Depends(http_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # декодируем токен
        return payload.get("sub")  # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое, что мы сами туда кладем
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass

# TODO Проверять токен
# Функция для получения пользовательских данных на основе имени пользователя
# def get_user(username: str):
#   for user in USERS_DATA:
#       if user.get("username") == username:
#            return user
#    return None


# роут для аутентификации; так делать не нужно, это для примера - более корректный пример в следующем уроке
'''
@app.post("/login")
async def login(user_in: User):
    for user in USERS_DATA:
        if user.get("username") == user_in.username and user.get("password") == user_in.password:
            return {"access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer"}
    return {"error": "Invalid credentials"}


# защищенный роут для получения информации о пользователе
@app.get("/about_me")
async def about_me(current_user: str = Depends(get_user_from_token)):
    user = get_user(current_user)
    if user:
        return user
    return {"error": "User not found"}
'''
