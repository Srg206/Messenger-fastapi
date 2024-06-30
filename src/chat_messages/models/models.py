import datetime
import pytz
from sqlalchemy import Date, DateTime, MetaData,Table,Column, Integer, String, ForeignKey, ARRAY, Time
from sqlalchemy.orm import relationship
#from __init__ import*
from .__init__ import Base
from zoneinfo import ZoneInfo
from src.chat_messages.models.association_models import User_Chat

def get_moscow_time():
    tz = pytz.timezone('Europe/Moscow')
    #datetime.
    return datetime.datetime.now

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False, default='chat')
    
    users = relationship('User', secondary='user_chat', back_populates='chats', passive_deletes=True)
    messages=relationship("Message", back_populates="chat",  passive_deletes=True)
        
    #users = Column(ARRAY(Integer),nullable=True)
    

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, index=True)
    content=Column(String)
    date=Column(Date, default=datetime.datetime.now().date, nullable=False)
    time = Column(DateTime, default=datetime.datetime.now, nullable=False)
    timezone=Column(String(500), nullable=False, default="Europe/Moscow")
    
    chat_id= Column(Integer, ForeignKey("chat.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id= Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True)
    
    chat=relationship("Chat", back_populates="messages")
    user=relationship("User", back_populates="messages")  
    



