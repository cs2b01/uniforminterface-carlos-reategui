from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Users(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(String(30))
    lastName = Column(String(50))
    password = Column(String(120))
