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
from src.work_with_info.router import info_router
from src.auth.router import auth_router
from src.chat_messages.message_router.message_router import *
#from src.chat_messages.chat_router import chat_router
from src.chat_messages.chat_router.chat_router import chat_router



app=FastAPI()
app.include_router(message_router)
app.include_router(chat_router)
app.include_router(info_router)
app.include_router(auth_router)

