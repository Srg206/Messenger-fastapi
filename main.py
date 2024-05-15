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



app=FastAPI()

load_dotenv()
SECRET_KEY=os.environ.get("SECRET_KEY")
ALGORITHM=os.environ.get("ALGORITHM")


#token_urls = ["login", "create"]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")

Abilities={"guest":"r",
      "user":"ru",
      "admin":"crud"
      }


class Client(BaseModel):
    role:str
    Client_name:str
    password:str

Clients ={
    "Pipister":Client(role="guest",Client_name="Pipister",password="1"),
    "Voprosi":Client(role="user",Client_name="Voprosi",password="2"),
    "C++ovich":Client(role="admin",Client_name="C++ovich",password="3")
}

notes=["mmmmm"] 


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token:str= Depends(oauth2_scheme)):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_token.get("sub")

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
    

@app.post("/create")
def create(token:str=Depends(decode_token), new_note:str=Body()):
    if token in Clients and 'c' in Abilities[Clients[token].role]:
        notes.append(new_note)
        return {"Added your note"}
    else:
        return {"Could not add your note"}

@app.get("/read")
def create(token:str=Depends(decode_token)):
    if token in Clients and 'r' in Abilities[Clients[token].role]:
        return notes
    else:
        return {"Could not give you notes"}

@app.post("/delete")
def create(token:str=Depends(decode_token)):
    if token in Clients and 'd' in Abilities[Clients[token].role]:
        notes.clear()
        return {"Deleted all notes"}
    else:
        return {"You Could not delete notes"}





@app.get("/unprotected")
def unprotected_data():
    return {"this is unprotected data, which can get everyone"}