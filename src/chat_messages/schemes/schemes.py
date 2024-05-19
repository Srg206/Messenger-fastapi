from pydantic import BaseModel

class Chat(BaseModel):
    email:str
    username:str
    password:str

class Message(BaseModel):
    content:str
    chat_id:str=None
    email:str=None

