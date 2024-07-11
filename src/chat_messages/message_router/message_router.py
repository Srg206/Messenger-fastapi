from fastapi import APIRouter, Body, Depends, HTTPException, Header, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from sqlalchemy import select, insert

from src.auth.models.models import User
from src.utils.utils import decode_token
from src.work_with_db.Check_access_to import check_access_to_chat
#from ..models.models import User
from ..schemes.schemes import *
from .__init__ import *
from ..models.models import *
import json
from ..ChatManager import ChatManager
from ..schemes.schemes import GotMsg, Msg_to_db
from ..SuperManager import spManager
from src.work_with_db.work_with_messages import *
from src.chat_messages.utils.utils import ConvertToPydentic


message_router = APIRouter(
    prefix="/msg",
    tags=["msg"]
)

AUTH_EX=HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
#chat_manager = ChatManager(name="ChatName", last_msg_id=0, users=[])


@message_router.get("/get_last_messages/{chat_id}")
async def get_last_chats(chat_id:int,token:str=Depends(decode_token)):
    session = sync_session
    if check_access_to_chat(token["sub"],chat_id):
        messages=session.query(Message).filter(Message.chat_id == chat_id).order_by(Message.time).limit(100).all()
    else:
        raise AUTH_EX
    print([ConvertToPydentic(msg) for msg in messages])
    return [ConvertToPydentic(msg) for msg in messages]
    
    


@message_router.post("/send_message")
async def send_message(new_msg: GotMsg):
    insert_message(new_msg)



#chat_manager=ChatManager()
@message_router.websocket("/get_msgs/{chat_id}")
async def websocket_endpoint(chat_id : int, websocket: WebSocket):
    chat_manager=spManager.active_connections[chat_id] 
    await chat_manager.connect(websocket)
    print(chat_manager.active_connections)    
    try:
        while True:
            data = await websocket.receive_text()
            print(chat_manager.active_connections)
            await chat_manager.broadcast(f"{data}")
    except WebSocketDisconnect as wsDis:
        print(wsDis)
        chat_manager.disconnect(websocket)
    except Exception as e:
        print(f"Unexpected error: {e}")
        await chat_manager.disconnect(websocket)


@message_router.get("/get_email_from_msgs/{chat_id}")
async def get_last_chats(chat_id:int,token:str=Depends(decode_token)):
    session = sync_session
    if check_access_to_chat(token["sub"],chat_id):
        messages=session.query(Message).filter(Message.chat_id == chat_id).order_by(Message.time).limit(100).all()
    else:
        raise AUTH_EX
    
    print([ConvertToPydentic(msg) for msg in messages])
    return [ConvertToPydentic(msg) for msg in messages]
    