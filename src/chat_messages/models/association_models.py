from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

#from src.auth.models.models import User
#from ..models.models import Base, Chat
from .__init__ import Base

    
class User_Chat(Base):
    __tablename__ = "user_chat"
    chat_id=Column(Integer, ForeignKey('chat.id',ondelete="CASCADE"), primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id',ondelete="CASCADE"), primary_key=True)
    
    

# class Msg_Chat(Base):
#     __tablename__ = "msg_chat"
#     chat_id=Column(Integer, ForeignKey('chat.id',ondelete="CASCADE"), primary_key=True)
#     msg_id=Column(Integer, ForeignKey('message.id',ondelete="CASCADE"), primary_key=True)
    
    
# class Msg_User(Base):
#     __tablename__ = "msg_user"
#     user_id=Column(Integer, ForeignKey('user.id',ondelete="CASCADE"), primary_key=True)
#     msg_id=Column(Integer, ForeignKey('message.id',ondelete="CASCADE"), primary_key=True)

 
