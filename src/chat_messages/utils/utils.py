
from mailbox import Message

from src.chat_messages.schemes.schemes import PydtcMessage


def ConverToPydentic(msg:Message):
    print("Conver_to_Pydentic")
    if(msg!=None):
        return PydtcMessage(id=msg.id,content=msg.content, chat_id=msg.chat_id, 
                            user_id=msg.user_id,date=str(msg.date)  , time=str(msg.time), timezone=msg.timezone)
    else:
        return None
