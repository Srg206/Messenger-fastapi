from pydantic import BaseModel

class CreateUser(BaseModel):
    email:str
    username:str
    password:str

class User_to_login(BaseModel):
    email:str
    password:str
    
class Tokens(BaseModel):
    access_token:str
    refresh_token:str

