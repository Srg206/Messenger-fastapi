import datetime
from sqlalchemy import DateTime, MetaData,Table,Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
#from __init__ import*
from .__init__ import Base
from zoneinfo import ZoneInfo

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False, default='chat')
    last_msg_id=Column(Integer,ForeignKey('message.id'), default=None)
    users = Column(ARRAY(Integer),nullable=True)
    

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, index=True)
    content=Column(String)
    chat_id=Column(Integer,ForeignKey('chat.id'), default=None)
    user_id=Column(Integer, ForeignKey('user.id'), default=None)
    time = Column(DateTime, default=datetime.datetime.now(ZoneInfo("Europe/Moscow")))

