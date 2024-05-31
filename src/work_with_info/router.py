from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel
from ..connection_to_postgres import *
from sqlalchemy import select, insert
from ..auth.models.models import User
from ..utils.utils import *
info_router = APIRouter(
    prefix="/work_with_info",
    tags=["work_with_info"]
)


Abilities={"guest":"r",
      "user":"ru",
      "admin":"crud"
      }


class Client(BaseModel):
    role:str
    Client_name:str
    password:str

Clients ={
    "Pipister":Client(role="guest",Client_name="Pipister",password="1"),
    "Voprosi":Client(role="user",Client_name="Voprosi",password="2"),
    "C++ovich":Client(role="admin",Client_name="C++ovich",password="3")
}

notes=["mmmmm"] 


@info_router.get("/read")
async def get_specific_operations(token:str=Depends(decode_token)):
    if token in Clients and 'r' in Abilities[Clients[token].role]:
        return notes
    else:
        return {"Could not give you notes"}


@info_router.get("/delete")
async def get_specific_operations(token:str=Depends(decode_token)):
    if token in Clients and 'd' in Abilities[Clients[token].role]:
        notes.clear()
        return {"Deleted all notes"}
    else:
        return {"You Could not delete notes"}
    

@info_router.post("/create")
def create(token:str=Depends(decode_token), new_note:str=Body()):
    if token in Clients and 'c' in Abilities[Clients[token].role]:
        notes.append(new_note)
        return {"Added your note"}
    else:
        return {"Could not add your note"}
