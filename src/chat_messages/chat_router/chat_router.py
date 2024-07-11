from typing import List
from fastapi import APIRouter, Body, Depends, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from sqlalchemy import select, insert

from src.auth.models.models import User
from src.utils.utils import decode_token
from ..schemes.schemes import CreateChat
from .__init__ import *
from ..models.models import *
import json
from ..ChatManager import ChatManager
from ..__init__ import *
from ..schemes.schemes import*
from ..SuperManager import spManager
from src.work_with_db.work_with_chats import*

chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)



@chat_router.post("/create_chat")
async def create_chat(new_chat:CreateChat):
    print(new_chat)
    return insert_new_chat(new_chat)        
    
@chat_router.get("/get_last_chats")
async def get_last_chats(token:str=Depends(decode_token)):
    got_email=token["sub"]
    return get_last_chats_by_email(got_email)
        
    
  
@chat_router.get("/get_email")
async def get_last_chats(token:str=Depends(decode_token)):
    return token["sub"]
        