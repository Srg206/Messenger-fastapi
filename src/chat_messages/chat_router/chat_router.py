from typing import List
from fastapi import APIRouter, Body, Depends, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from sqlalchemy import select, insert

from src.auth.models.models import User
from src.utils.utils import decode_token
#from ..models.models import User
from ..schemes.schemes import CreateChat
from .__init__ import *
from ..models.models import *
import json
from ..ChatManager import ChatManager
from ..__init__ import *
from ..schemes.schemes import*

from ..SuperManager import spManager


chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

def ConverToPydentic(msg:Message):
    print("ok")
    if(msg!=None):
        return PydtcMessage(id=msg.id,content=msg.content, chat_id=msg.chat_id, 
                            user_id=msg.user_id,date=str(msg.date)  , time=str(msg.time), timezone=msg.timezone)
    else:
        return None
        


@chat_router.post("/create_chat")
async def create_chat(new_chat:CreateChat):
    print(new_chat)
    session = sync_session
    new_record = Chat(name=new_chat.name, users= new_chat.users )
    session.add(new_record)
    session.commit()
    
    print(new_record.id)
    timezone_str = 'Europe/Moscow'

    greeting = Message(
        content="HELLO EVERYBODY",
        chat_id=new_record.id,
        timezone=timezone_str  # Ensure this is a string
    )

    #greeting=Message(content="HELLO EVERYBODY", chat_id=new_record.id )
    print(greeting)
    
    session.add(greeting)  
    session.flush()
    chat = session.query(Chat).filter(Chat.id==new_record.id).first().last_msg_id=greeting.id
    session.commit()
    
    chat_id =new_record.id
    print(new_chat.users)
    print("chat id is ---- ",chat_id)
    
    for user_id in new_chat.users:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            if user.chats is None:
                user.chats = []
            user.chats.append(chat_id)
            session.commit()
            print(user.chats)
    for user_id in new_chat.users:
        user = session.query(User).filter(User.id == user_id).first()
        print(user.chats)
    session.commit()
    session.close()
        
    
@chat_router.get("/get_last_chats")
async def get_last_chats(token:str=Depends(decode_token)):
    got_gmail=token["sub"]
    session = sync_session
    print(got_gmail)
    chats_id=session.query(User).filter_by(email=got_gmail).first().chats
    chats = session.query(Chat).filter(Chat.id.in_(chats_id)).all()
    this_user_chats=[]
    print(chats[0].id)
    for x in chats:
        print(session.query(Message).filter_by(id=x.last_msg_id).first().id)
        last_message=ConverToPydentic(session.query(Message).filter_by(id=x.last_msg_id).first())
        print(last_message)
        cur_chat={'chat_name':x.name,"last_message":last_message,'chat_id':x.id}
        this_user_chats.append(cur_chat)
    
    this_user_chats = sorted(this_user_chats, key=lambda x: x['last_message'].time)
    return this_user_chats
        
    
    
    
    
    
    
    
    
    

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

        