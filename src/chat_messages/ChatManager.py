from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from .schemes.schemes import GlobalChat



class ChatManager:
    def __init__(self, id:int,name:str, last_msg_id:int, users:List[int] ):
        self.active_connections: list[WebSocket] = []
        self.related_chat=GlobalChat(id,name,last_msg_id,users)  

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # async def send_personal_message(self, message: str, websocket: WebSocket):
    #     await websocket.send_text(message)
    
    # async def broadcast(self, message: str):
    #     for connection in self.active_connections:
    #         await connection.send_text(message)
    
    async def send_active_chat_users(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
#manager = ConnectionManager()
