from fastapi import FastAPI, Header, Depends
from fastapi.responses import FileResponse

from database import create_tables, delete_tables
from models.models import Answer, Product, ListOfProducts, ProductAdd
from fastapi.staticfiles import StaticFiles
from typing import Annotated
# from routers.create_db import Users
import hashlib
from contextlib import asynccontextmanager
from routers.routers import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

app.include_router(user_router)






