from sqlalchemy import MetaData,Table,Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from src.chat_messages.models.association_models import *
from src.chat_messages.models.models import Chat
from .__init__ import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False, default='user')
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
     
     
    chats = relationship('Chat', secondary='user_chat', back_populates='users', passive_deletes=True)
    messages=relationship("Message", back_populates="user",  passive_deletes=True)



    