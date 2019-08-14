#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False) 
    cities = relationship("City", backref="state")

@property
def cities(self):
    """getter for citties
    """
    my_list = []
    for ids in self.cities:
        if ids.state_id == self.id:
            my_list.append(ids)
    return my_list