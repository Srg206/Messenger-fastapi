from src.config import Postgres_asyncpg_URL, Postgres_psycopg_URL
from src import connection
from src import *
from src.connection import *
from sqlalchemy import String, create_engine, text
from src.config import Postgres_asyncpg_URL, Postgres_psycopg_URL



connection = sync_engine.connect()
connection.execute(text("CREATE TABLE accounts (user_id SERIAL PRIMARY KEY, username VARCHAR (50) UNIQUE NOT NULL);"))
print('ffff')
connection.close()