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
        
    
   
    
    
    

# @auth_router.post("/create_user")
# def login(user_data: CreateUser):
#     print("create_user")
#     session = sync_session
#     if (session.query(User).filter_by(email=user_data.email).first() is None):
#         hashed_password = encode_password(user_data.password)
#         new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
#         session.add(new_record)
#         session.commit()
#         session.close()
#         return {"access_token": create_jwt_token({"sub": user_data.email})}
#     else:
#         return{"error": "Invalid credentials"}

    
# @chat_router.websocket("/get")
# async def websocket_endpoint(websocket: WebSocket):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"You wrote: {data}", websocket)
#             await manager.broadcast(f"{data}")
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"Client left the chat")


        
# # @message_router.websocket("/get")
# # async def websocket_endpoint(websocket):
# #     await websocket.accept()
# #     while True:
# #         new_msg = await websocket.receive()
# #         data=json.loads(new_msg)
# #         session = sync_session
# #         new_record = Message(content=new_msg.content)
# #         session.add(new_record)
# #         session.commit()
# #         await websocket.send_text(f"Message text was: {new_msg.content}")


# # @message_router.websocket("/get")
# # def chat_working(user_data: CreateUser):
# #     print("create_user")
# #     Session = sessionmaker(bind=sync_engine)
# #     session = Session()
# #     if (session.query(User).filter_by(email=user_data.email).first() is None):
# #         hashed_password = encode_password(user_data.password)
# #         new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
# #         session.add(new_record)
# #         session.commit()
# #         session.close()
# #         return {"access_token": create_jwt_token({"sub": user_data.email})}
# #     else:
# #         return{"error": "Invalid credentials"}

        