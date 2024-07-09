from fastapi import *
from src.auth.router import auth_router
from src.chat_messages.message_router.message_router import *
from src.chat_messages.chat_router.chat_router import chat_router

from fastapi.middleware.cors import CORSMiddleware

#from src.chat_messages.chat_router import chat_router

app=FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://127.0.0.1:8000",
    "https://193.124.115.115",
    "http://127.0.0.1:8000/auth/login"
]


#origins = ["http://127.0.0.1:4000"]

# Add CORS middleware to your app
app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth_router)
app.include_router(message_router)
app.include_router(chat_router)


