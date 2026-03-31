from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from api.db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

# Table create
Base.metadata.create_all(bind=engine)