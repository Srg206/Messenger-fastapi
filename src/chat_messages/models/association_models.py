from sqlalchemy import Column, Integer, Table, ForeignKey
from ..models.models import Base

class User_Chat(Base):
    __tablename__ = "user_chat"
    chat_id=Column(Integer, ForeignKey('chat.id'), primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'), primary_key=True)
    
