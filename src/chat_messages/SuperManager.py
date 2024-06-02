from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from src.chat_messages.ChatManager import ChatManager

class SuperManager:
    def __init__(self):
        self.active_connections: list[ChatManager] = []

    async def create_new_chat(self, new_chat_mng:ChatManager):
        self.active_connections.append(new_chat_mng)

spManager=SuperManager()
