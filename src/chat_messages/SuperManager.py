from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import Dict

from src.chat_messages.ChatManager import ChatManager
from src.chat_messages.models.models import Chat
from ..connection_to_postgres import *

class SuperManager:
    def __init__(self):
        self.active_connections: Dict[int, ChatManager]={}
        session = sync_session
        chat_ids = session.query(Chat.id).all()
        chat_ids_list = [id[0] for id in chat_ids]        
        for x in chat_ids_list:
            if x not in self.active_connections:
                self.active_connections[x]=ChatManager()

        
                
        
    async def create_new_chat(self, new_chat_mng:ChatManager):
        self.active_connections.append(new_chat_mng)

spManager=SuperManager()
