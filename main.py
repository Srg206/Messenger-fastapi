from src.config import Postgres_asyncpg_URL, Postgres_psycopg_URL
from src import connection
from src import *
from src.connection import *
from sqlalchemy import String, create_engine, text
from src.config import Postgres_asyncpg_URL, Postgres_psycopg_URL
from src.models.models import User
from src.schemes.schemes import CreateUser, LoginUser
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



app=FastAPI()

app.include_router(info_router)



@app.post("/create_user")
def login(user_data: CreateUser):
    print("create_user")
    Session = sessionmaker(bind=sync_engine)
    session = Session()
    if (session.query(User).filter_by(email=user_data.email).first() is None):
        hashed_password = encode_password(user_data.password)
        new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
        session.add(new_record)
        session.commit()
        session.close()
        return {"access_token": create_jwt_token({"sub": user_data.email})}
    else:
        return{"error": "Invalid credentials"}

        

@app.post("/login")
def login(user_data: LoginUser):
    Session = sessionmaker(bind=sync_engine)
    session = Session()
    found_user=session.query(User).filter_by(email=user_data.email).first() 
    print(user_data.password)
    if (found_user is not None) and verify_password(user_data.password,found_user.password):
        return {"access_token": create_jwt_token({"sub": user_data.email})}
    else:
        return{"error": "Invalid credentials"}
    

