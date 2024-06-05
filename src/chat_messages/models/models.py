import datetime
import pytz
from sqlalchemy import Date, DateTime, MetaData,Table,Column, Integer, String, ForeignKey, ARRAY, Time
from sqlalchemy.orm import relationship
#from __init__ import*
from .__init__ import Base
from zoneinfo import ZoneInfo

def get_moscow_time():
    tz = pytz.timezone('Europe/Moscow')
    #datetime.
    return datetime.datetime.now

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False, default='chat')
    last_msg_id=Column(Integer,ForeignKey('message.id'), default=None,nullable=True)
    users = Column(ARRAY(Integer),nullable=True)
    

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, index=True)
    content=Column(String)
    chat_id=Column(Integer,ForeignKey('chat.id'), default=None)
    user_id=Column(Integer, ForeignKey('user.id'), default=None,nullable=True)
    date=Column(Date, default=datetime.datetime.now().date, nullable=False)
    time = Column(DateTime, default=datetime.datetime.now, nullable=False)
    timezone=Column(String(500), nullable=False)
    #time = Column(DateTime,  default=lambda: datetime.now(ZoneInfo("Europe/Moscow")))

