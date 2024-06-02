from typing import List
from pydantic import BaseModel
from datetime import time


class GlobalChat(BaseModel):
    id: int
    name:str
    last_msg_id:int
    users:List[int]
    
    
class CreateChat(BaseModel):
    name:str
    users: List[int]

    
class Message(BaseModel):
    id:int
    content:str
    chat_id:int
    user_id:int
    time:time
