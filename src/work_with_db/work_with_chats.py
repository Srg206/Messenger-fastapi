from typing import List
from src.auth.models.models import User
from src.chat_messages.models.models import Chat, Message
from src.chat_messages.schemes.schemes import CreateChat
from ..connection_to_postgres import *
from src.chat_messages.models.association_models import User_Chat
from ..chat_messages.message_router.message_router import *




def insert_new_chat(new_chat:CreateChat):
    session = sync_session
    new_record = Chat(name=new_chat.name)
    session.add(new_record)
    session.flush()
    
    spManager.active_connections[new_record.id]=ChatManager()
    
    add_users_by_id(new_chat.users,new_record, session)
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
    session.close()
    
    
    
def add_users_by_id(users,chat:Chat, session ):
    this_chat_users=session.query(User).filter(User.id.in_(users)).all()
    for user in this_chat_users:
        chat.users.append(user)
        
    
    