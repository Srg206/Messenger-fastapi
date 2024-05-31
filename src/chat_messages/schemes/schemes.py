from pydantic import BaseModel
from datetime import time

class Chat(BaseModel):
    id:int
    name:str
    last_msg_id:int

class Message(BaseModel):
    id:int
    content:str
    chat_id:int
    user_id:int
    time:time
