from fastapi import HTTPException
from src.auth.models.models import User
from src.chat_messages.models.models import Chat, Message
from src.chat_messages.schemes.schemes import GotMsg
from src.utils.utils import decode_token
from src.work_with_db.Check_access_to import check_access_to_chat
from ..connection_to_postgres import sync_session
from ..chat_messages.models.association_models import User_Chat


def insert_message(new_msg: GotMsg):
    session = sync_session
    email=decode_token(new_msg.token)['sub']
    user=session.query(User).filter(User.email==email).first()
    chat=session.query(Chat).filter(Chat.id==new_msg.chat_id).first()
    if check_access_to_chat(user.email, chat.id):
        db_msg=Message(
            content=new_msg.content,
            chat_id=new_msg.chat_id,
            user_id=user.id,
            timezone='Europe/Moscow'
        )
        session.add(db_msg)  
        session.flush()
        
        db_msg.user=user
        db_msg.chat=chat
        print(db_msg.chat_id)
        user.messages.append(db_msg)
        chat.messages.append(db_msg)
        session.commit()
        session.close()
    else:
        raise HTTPException(
            status_code=1000,
            detail="You do not have access to this chat",
        )
