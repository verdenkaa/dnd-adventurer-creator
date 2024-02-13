from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session



Base = declarative_base()

class Race(Base):
    __tablename__ = "Race"
    Name = Column(String, primary_key=True)

class Class(Base):
    __tablename__ = "Class"
    Name = Column(String, primary_key=True)

