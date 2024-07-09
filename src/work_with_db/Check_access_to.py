from src.chat_messages.models.association_models import User_Chat
from src.connection_to_postgres import sync_session
from src.auth.models.models import User
from src.chat_messages.models.models import Chat


def check_access_to_chat(user_email: str,chat_ind: int):
    session=sync_session
    query = session.query(User_Chat).filter(User_Chat.chat_id==chat_ind).all()
    user_id=session.query(User).filter(User.email==user_email).first().id
    users=[x.user_id for x in query]
    return user_id in users
