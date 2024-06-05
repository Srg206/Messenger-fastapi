from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column
from typing import Annotated
Base = declarative_base()

metadata=MetaData()
intpk=Annotated[int,mapped_column(primary_key=True)]
