import asyncio
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import String, create_engine, text
from .config import Postgres_asyncpg_URL, Postgres_psycopg_URL


sync_engine= create_engine(
    url=Postgres_psycopg_URL()
)

async_engine=create_async_engine(
    url=Postgres_asyncpg_URL()
)
