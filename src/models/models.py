from sqlalchemy import MetaData,Table,Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

metadata=MetaData()


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role_id=Column(Integer, ForeignKey('role.id'))
    role=relationship("Role")


class www(Base):
    __tablename__ = 'www'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  nullable=False)

