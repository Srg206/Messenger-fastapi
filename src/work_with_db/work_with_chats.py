from src.auth.models.models import User
from src.chat_messages.models.models import Chat, Message
from src.chat_messages.schemes.schemes import CreateChat
from ..connection_to_postgres import *
from src.chat_messages.models.association_models import user_chat





def insert_new_chat(new_chat:CreateChat):
    session = sync_session
    new_record = Chat(name=new_chat.name, users= new_chat.users )
    session.add(new_record)
    session.flush()
    Chat_created_message = Message(
        content="HELLO EVERYBODY",
        chat_id=new_record.id,
        timezone='Europe/Moscow'
    )

    session.add(Chat_created_message)  
    session.flush()
    chat = session.query(Chat).filter(Chat.id==new_record.id).first().last_msg_id=Chat_created_message.id
    session.commit()
    
    chat_id =new_record.id
    print(new_chat.users)
    print("chat id is ---- ",chat_id)
    
    users = session.query(User).filter(User.id.in_(new_chat.users)).all()
    #print("users - ",users)
    for user in users:
        #user_chat.
        user.chats.append(chat_id)
    session.commit()
    for user in users:
        session.refresh(user)
        
    # for user_id in new_chat.users:
    #     user = session.query(User).filter(User.id == user_id).first()
    #     if user:
    #         if user.chats is None:
    #             user.chats = []
    #         user.chats.append(new_record.id)
    #         session.commit()
    #         #session.refresh(user)
    #         print(user.chats)
    
    session.commit()
    for user_id in new_chat.users:
        user = session.query(User).filter(User.id == user_id).first()
        print(user.chats)
    session.commit()
    session.close()