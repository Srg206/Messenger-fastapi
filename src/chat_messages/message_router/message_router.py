# from fastapi import APIRouter, Body, Depends
# from pydantic import BaseModel
# from ..connection import *
# from sqlalchemy import select, insert
# from ..models.models import User
# from ..utils.utils import *
# from .schemes.schemes import CreateUser, LoginUser
# message_router = APIRouter(
#     prefix="/msg",
#     tags=["msg"]
# )




# @message_router.post("/create_user")
# def login(user_data: CreateUser):
#     print("create_user")
#     Session = sessionmaker(bind=sync_engine)
#     session = Session()
#     if (session.query(User).filter_by(email=user_data.email).first() is None):
#         hashed_password = encode_password(user_data.password)
#         new_record = User(name=user_data.username, email=user_data.email, password=hashed_password)
#         session.add(new_record)
#         session.commit()
#         session.close()
#         return {"access_token": create_jwt_token({"sub": user_data.email})}
#     else:
#         return{"error": "Invalid credentials"}

        

# @message_router.post("/login")
# def login(user_data: LoginUser):
#     Session = sessionmaker(bind=sync_engine)
#     session = Session()
#     found_user=session.query(User).filter_by(email=user_data.email).first() 
#     print(user_data.password)
#     if (found_user is not None) and verify_password(user_data.password,found_user.password):
#         return {"access_token": create_jwt_token({"sub": user_data.email})}
#     else:
#         return{"error": "Invalid credentials"}