import jwt
from env import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPBearer
from fastapi import Depends

http_bearer = HTTPBearer()


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def get_user_from_token(token=Depends(http_bearer)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("id")
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        print(jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]))
        return False
