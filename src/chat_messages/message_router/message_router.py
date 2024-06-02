from fastapi import APIRouter, Body, Depends, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from sqlalchemy import select, insert

from src.auth.models.models import User
from src.utils.utils import decode_token
#from ..models.models import User
from ..schemes.schemes import *
from .__init__ import *
from ..models.models import *
import json
from ..ChatManager import ChatManager
message_router = APIRouter(
    prefix="/msg",
    tags=["msg"]
)


@message_router.get("/get_last_messages")
async def get_last_chats(chat_id:int):
    session = sync_session
    messages=session.query(Message).order_by(Message.time).limit(100).all()
    return messages     
    

@message_router.websocket("/get_msgs/")
async def websocket_endpoint(chat_id : int, websocket: WebSocket):
    await ChatManager.connect(websocket)
    try:
        while True:
            msg=WebSocket.receive_json
            data = await websocket.receive_text()
            await ChatManager.send_personal_message(f"You wrote: {data}", websocket)
            await ChatManager.broadcast(f"{data}")
    except WebSocketDisconnect:
        ChatManager.disconnect(websocket)
        await ChatManager.broadcast(f"Client left the chat")


        
# @message_router.websocket("/get")
# async def websocket_endpoint(websocket):
#     await websocket.accept()
#     while True:
#         new_msg = await websocket.receive()
#         data=json.loads(new_msg)
#         session = sync_session
#         new_record = Message(content=new_msg.content)
#         session.add(new_record)
#         session.commit()
#         await websocket.send_text(f"Message text was: {new_msg.content}")


# @message_router.websocket("/get")
# def chat_working(user_data: CreateUser):
#     print("create_user")
#     Session = sessionmaker(bind=sync_engine)
#     session = Session()
#     if (session.query(User).filter_by(email=user_data.email).first() is None):
#         hashed_password = encode_password(user_data.password)
#         new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
#         session.add(new_record)
#         session.commit()
#         session.close()
#         return {"access_token": create_jwt_token({"sub": user_data.email})}
#     else:
#         return{"error": "Invalid credentials"}

        