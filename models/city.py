#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from sqlachemy.ext.declarative import declarative_base
from sqlachemy import Column, Integer, String, ForeignKey 

Base = declarative_base()

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"

    name = Column(String(128)), (nullable=False))
    state_id = Column(ForeignKey("states.id") , String(60),(nullable=False))
