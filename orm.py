from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

from flask_sqlalchemy import SQLAlchemy
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)