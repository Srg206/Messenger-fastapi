from sqlalchemy import MetaData,Table,Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#from __init__ import*

Base = declarative_base()

metadata=MetaData()



class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False, default='chat')

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, index=True)
    content=Column(String)
    chat_id=Column(Integer,ForeignKey('chat.id'), default=None)
    user_id=Column(Integer, ForeignKey('user.id'), default=None)


