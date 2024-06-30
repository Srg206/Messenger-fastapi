from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel
from ..connection_to_postgres import * # type: ignore
from sqlalchemy import select, insert
from .models.models import User
from ..utils.utils import *
from .schemes.schemes import CreateUser, LoginUser
from ..connection_to_postgres import *


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)




@auth_router.post("/create_user")
def login(user_data: CreateUser):
    print("create_user")
    session = sync_session
    try:
        user_exist= not(session.query(User).filter_by(email=user_data.email).first() is None)
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        )
    if (not user_exist):
        try:
            hashed_password = encode_password(user_data.password)
            new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
            session.add(new_record)
            session.commit()
            session.close()
            return {"access_token": create_jwt_token({"sub": user_data.email})}
        except:
            raise HTTPException(
            status_code=500,
            detail="Internal server error",
        )         
    else:
         raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        

@auth_router.post("/login")
def login(user_data: LoginUser):
    print('login')
    session = sync_session
    try:
        found_user=session.query(User).filter_by(email=user_data.email).first() 
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        )
        
    #print(verify_password(user_data.password,found_user.password))
    if (found_user is not None) and verify_password(user_data.password,found_user.password):
        token=create_jwt_token({"sub": user_data.email})
        print(token)
        return {"access_token": token }
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )