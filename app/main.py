from fastapi import FastAPI, Header, Depends
from fastapi.responses import FileResponse

from database import create_tables, delete_tables
from models.models import Answer, Product, ListOfProducts
from fastapi.staticfiles import StaticFiles
from typing import Annotated
# from routers.create_db import Users
import hashlib
from contextlib import asynccontextmanager
from routers.routers import router as user_router
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:5173",
]



@asynccontextmanager
async def lifespan(app: FastAPI):
    #await delete_tables()
    await create_tables()
    print("Перезапуск")
    yield


app = FastAPI(lifespan=lifespan)

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
