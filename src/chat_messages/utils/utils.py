from src.auth.models.models import User
from src.chat_messages.models.models import Message
from src.chat_messages.schemes.schemes import PydtcMessage
from src.connection_to_postgres import sync_session

def ConvertToPydentic(msg:Message):
    print("Conver_to_Pydentic")
    if(msg!=None):
        email=sync_session.query(User).filter_by(id=msg.user_id).first().email
        return PydtcMessage(id=msg.id,content=msg.content, chat_id=msg.chat_id, 
                            user_id=msg.user_id,date=str(msg.date)  , time=str(msg.time), timezone=msg.timezone, email=email)
    else:
        return None
