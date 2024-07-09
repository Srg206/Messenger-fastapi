import time
from fastapi import Depends, HTTPException, Response
from src.auth.models.models import User
#from src.auth.router import AUTH_EX, SERV_EX
from src.utils.utils import create_jwt_token, decode_token, verify_password
from ..connection_to_postgres import sync_session
from sqlalchemy.orm import Session
from ..auth.schemes.schemes import Tokens, User_to_login
from dotenv import load_dotenv
import os
from typing import Dict
load_dotenv()

POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
ACCESS_TOKEN_EXPIRE_TIME=os.environ.get("ACCESS_TOKEN_EXPIRE_TIME")
REFRESH_TOKEN_EXPIRE_TIME=os.environ.get("REFRESH_TOKEN_EXPIRE_TIME")



SERV_EX=HTTPException(
            status_code=500,
            detail="Internal server error",
        )
AUTH_EX=HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
DB_SERV_EX=HTTPException(
            status_code=500,
            detail="Internal server error DB",
        )
#Tokens_bd: Dict[str, Tokens]={}
Tokens_bd: Dict[str, str]={}

def Login_User(user_data: User_to_login,response: Response):
    found_user=Email_in_bd(user_data.email)
    if found_user and verify_password(user_data.password,found_user.password):
        access_token=create_jwt_token({"sub": user_data.email, "created_at": round(time.time())})
        refresh_token=create_jwt_token({"sub": user_data.email, "created_at": round(time.time())})
        print(access_token, refresh_token)
        save_tokens(access_token=access_token,refresh_token=refresh_token)
        print(access_token)
        response.set_cookie(access_token)
        return access_token
    else:
        raise AUTH_EX

def Cookie_is_Valid(access_token:str):
    print(Tokens_bd)
    atoken=decode_token(access_token)
    session = sync_session
    if Email_in_bd(atoken["sub"]):
        return validate_access_token(access_token)# if None that means we should login with pass
    else:
        raise AUTH_EX


def validate_access_token(access_token:str): # check 
    old_access_token=access_token
    
    if access_token not in Tokens_bd:
        return None
    refresh_token=Tokens_bd[access_token]
    
    atoken=decode_token(access_token)
    refresh_token=update_refresh_token(refresh_token)
    if not refresh_token: # In this case we should ask user to login with password again
        return None
    
    if int(atoken["created_at"])+int(ACCESS_TOKEN_EXPIRE_TIME)<int(round(time.time())):
        access_token=create_jwt_token({"sub": atoken["sub"], "created_at": round(time.time())})
        save_tokens(old_access_token=old_access_token,access_token=access_token, refresh_token=refresh_token)
        
    return access_token


def update_refresh_token(token:str):
    dtoken=decode_token(token)
    if Email_in_bd(dtoken["sub"]):
        if int(dtoken["created_at"])+int(REFRESH_TOKEN_EXPIRE_TIME)>int(round(time.time())):
            refresh_token=token
        else:
            refresh_token=None # In this case we should ask user to login with password again
        return refresh_token
    else:
        return AUTH_EX

def save_tokens( access_token, refresh_token, old_access_token=None):
    if old_access_token !=None:
        if old_access_token not in Tokens_bd:
            raise DB_SERV_EX
        del Tokens_bd[old_access_token]
    Tokens_bd[access_token] = refresh_token

def Email_in_bd(myemail:str):
    session=sync_session
    try:
        found_user=session.query(User).filter_by(email=myemail).first() 
    except:
        raise SERV_EX
    return found_user





# def generate_access_token(email):
#     retrun 
    
    
# def create_jwt_token(data: dict):
#     return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# def generate_refresh_token():
    