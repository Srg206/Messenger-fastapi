from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel
from ..connection import *
from sqlalchemy import select, insert
from ..models.models import User
from ..utils.utils import *
from .schemes.schemes import CreateUser, LoginUser
from ..connection import *

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)




@auth_router.post("/create_user")
def login(user_data: CreateUser):
    print("create_user")
    session = sync_session
    if (session.query(User).filter_by(email=user_data.email).first() is None):
        hashed_password = encode_password(user_data.password)
        new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
        session.add(new_record)
        session.commit()
        session.close()
        return {"access_token": create_jwt_token({"sub": user_data.email})}
    else:
        return{"error": "Invalid credentials"}

        

@auth_router.post("/login")
def login(user_data: LoginUser):
    session = sync_session
    found_user=session.query(User).filter_by(email=user_data.email).first() 
    print(user_data.password)
    if (found_user is not None) and verify_password(user_data.password,found_user.password):
        return {"access_token": create_jwt_token({"sub": user_data.email})}
    else:
        return{"error": "Invalid credentials"}