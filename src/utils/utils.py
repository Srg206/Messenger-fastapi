import os
import bcrypt
from dotenv import find_dotenv, load_dotenv
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt


load_dotenv(find_dotenv())
load_dotenv()
SECRET_KEY=os.environ.get("SECRET_KEY")
ALGORITHM=os.environ.get("ALGORITHM")
SALT=os.environ.get("SALT")


#salt=bcrypt.gensalt()
#print(salt)

def encode_password(new_password:str):
    print("START ENCODE")
    strValue = bcrypt.hashpw(new_password.encode(), SALT.encode('utf-8')).decode('UTF-8')
    print("FINISH ENCODE") 
    return strValue


def verify_password(password, old_password):
    print("VERIFY")
    hashed_pass = encode_password(password)
    print(hashed_pass)
    print(old_password)
    return hashed_pass==old_password



#token_urls = ["login", "create"]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="") # tokenUrl это url по которым можно выпустить токен




def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token:str= Depends(oauth2_scheme)):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_token

