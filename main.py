from src.config import Postgres_asyncpg_URL, Postgres_psycopg_URL
from src import connection_to_postgres
from src import *
from src.connection_to_postgres import *
from sqlalchemy import String, create_engine, text
from src.config import Postgres_asyncpg_URL, Postgres_psycopg_URL
from src.utils.utils import encode_password,verify_password
from datetime import datetime
from typing import List, Union

from pydantic import BaseModel
from fastapi import *
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import jwt
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os
from src.utils.utils import *
from src.auth.router import auth_router
from src.chat_messages.message_router.message_router import *
#from src.chat_messages.chat_router import chat_router
from src.chat_messages.chat_router.chat_router import chat_router
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://127.0.0.1:8000",
    "https://193.124.115.115",
    "http://127.0.0.1:8000/auth/login"
]


#origins = ["http://127.0.0.1:4000"]

# Add CORS middleware to your app
app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(message_router)
app.include_router(chat_router)
app.include_router(auth_router)

