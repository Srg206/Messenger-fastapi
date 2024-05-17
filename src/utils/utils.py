import os
import bcrypt
from dotenv import load_dotenv
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

salt=bcrypt.gensalt()
def encode_password(new_password:str):
    print("START ENCODE")
    strValue = bcrypt.hashpw(new_password.encode(), salt).decode('UTF-8')
    print(new_password)
    print(strValue)
    print("FINISH ENCODE") 
    return strValue


def verify_password(password, old_password):
    print("VERIFY")
    hashed_pass = encode_password(password)
    print(hashed_pass)
    print(old_password)
    return hashed_pass==old_password

load_dotenv()
SECRET_KEY=os.environ.get("SECRET_KEY")
ALGORITHM=os.environ.get("ALGORITHM")


#token_urls = ["login", "create"]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")




def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token:str= Depends(oauth2_scheme)):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

