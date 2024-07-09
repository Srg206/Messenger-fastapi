from typing import List
from src.auth.models.models import User
from src.chat_messages.models.models import Chat, Message
from src.chat_messages.schemes.schemes import CreateChat
from src.chat_messages.utils.utils import ConvertToPydentic
from ..connection_to_postgres import *
from src.chat_messages.models.association_models import User_Chat
from ..chat_messages.message_router.message_router import *




def insert_new_chat(new_chat:CreateChat):
    session = sync_session
    new_record = Chat(name=new_chat.name)
    session.add(new_record)
    session.flush()
    
    spManager.active_connections[new_record.id]=ChatManager()
    
    add_users_by_email(new_chat.users,new_record, session)
    session.flush()
    
    
    Chat_created_message = Message(
        content="HELLO EVERYBODY",
        chat_id=new_record.id,
        user_id=1,
        timezone='Europe/Moscow'
    )

    session.add(Chat_created_message)  
    session.flush()
    new_record.messages.append(Chat_created_message)
    session.commit()
    last_message=ConvertToPydentic(Chat_created_message)
    created_chat={'chat_name':new_chat.name,"last_message":last_message,'chat_id':new_record.id}
    session.close()
    return created_chat
    
 
def get_last_chats_by_email(gotemail:str):
    session = sync_session
    print(gotemail)
    chats=session.query(User).filter_by(email=gotemail).first().chats
    
    this_user_chats=[]
    for x in chats:
        last_message=ConvertToPydentic(x.messages[-1])
        print(last_message)
        cur_chat={'chat_name':x.name,"last_message":last_message,'chat_id':x.id}
        this_user_chats.append(cur_chat)
    this_user_chats = sorted(this_user_chats, key=lambda x: x['last_message'].time, reverse=True)
    return this_user_chats
    
    
def add_users_by_email(users,chat:Chat, session ):
    this_chat_users=session.query(User).filter(User.email.in_(users)).all()
    for user in this_chat_users:
        chat.users.append(user)
        