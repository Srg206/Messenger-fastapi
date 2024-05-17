import asyncio
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, session
from typing import AsyncGenerator, Generator
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import String, create_engine, text
from .config import Postgres_asyncpg_URL, Postgres_psycopg_URL


sync_engine= create_engine(
    url=Postgres_psycopg_URL()
)

async_engine=create_async_engine(
    url=Postgres_asyncpg_URL()  
)

async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


session_maker = sessionmaker(bind=sync_engine, expire_on_commit=False)
def get_session() -> Generator[Session, None, None]:
    with session_maker() as session:
        yield session
        

