from fastapi import APIRouter, Body, Depends, HTTPException, Response
from pydantic import BaseModel
from ..connection_to_postgres import * # type: ignore
from sqlalchemy import select, insert
from .models.models import User
from ..utils.utils import *
from .schemes.schemes import CreateUser, User_to_login,VerificationInfo
from ..connection_to_postgres import *
from src.work_with_db.work_with_users import *
from .utils import *


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SERV_EX=HTTPException(
            status_code=500,
            detail="Internal server error",
        )
AUTH_EX=HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


@auth_router.post("/create_user")
def login(user_data: CreateUser, response: Response):
    print("create_user")
    session = sync_session
    try:
        user_exist= not(session.query(User).filter_by(email=user_data.email).first() is None)
    except:
        raise SERV_EX
    if (not user_exist):
        try:
            Send_verification_number(user_data.email)
            return {"Success"}
            # return {"access_token": access_token}
        except Exception as e:
            print(e)
            raise SERV_EX
    else:
         raise AUTH_EX
    

@auth_router.post("/verify_code")
def verification(code:VerificationInfo,user_data: CreateUser,response:Response):
    print('verification')
    if verify_code(code.code,user_data.email):
        session = sync_session
        hashed_password = encode_password(user_data.password)
        new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
        session.add(new_record)
        after_register_access_token= Login_User(user_data=User_to_login(email=user_data.email, password=user_data.password),response=response)
        session.commit()
        session.close()
        return {"access_token": after_register_access_token}
    else:
        raise AUTH_EX



@auth_router.post("/login_by_pass")
def login(user_data: User_to_login,response: Response):
    print('login_by_pass')
    session = sync_session
    access_token= Login_User(user_data=user_data,response=response)
    return {"access_token": access_token}
    

@auth_router.post("/validate_cookie")
def validate_cookie( response: Response, token:str=Depends(decode_token)):
    token=create_jwt_token({"sub": token["sub"], "created_at": token["created_at"]})
    print('validate_cookie')
    res_jwt=Cookie_is_Valid(token)
    response.set_cookie(res_jwt)
    return {"access_token":res_jwt}
    