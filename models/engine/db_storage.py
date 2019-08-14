#!/usr/bin/python3
"""This is DB_Storage Engine"""
import pip
import os
from models.base_model import BaseModel
from sqlachemy.ext.declarative import declarative_base
from sqlachemy import Column, Integer, String, ForeignKey
from sqlachemy.orm import sessionmaker
from sqlachemy.orm import scoped_session
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine

class DBStorage:
    """SQL STORAGE ENGINE
    """
    __engine = None
    __session = None

    def __init__(self):
        """ create the engine
        """
        user= os.environ.get("username")
        password= os.environ.get("HBNB_MYSQL_PWD")
        localhost=os.enivron.get("localhost")
        database= os.environ.get("database")
        
        eng = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                        (user, password, database, localhost, 
                         pool_pre_ping=True))

        Session = sessionmaker(bind=eng)
        sesh = Session()

    def all(self, cls=None):
        """ method that returns everyting based on class name
        """
        a_dict = {}
        sesh.query(cls.__name__).all() 
        if not cls:
            return self.__session
        else:
             my_dict = {}
             for key, value in self.__objects.items():
                 if key.startswith(cls.__name__):
                     my_dict[cls.__name__] = value
        return my_dict

    def new(self, obj):
        """ add object to current database
        """
        #for k, v in self.__object.items():
        sesh.add(obj)
        sesh.commit(obj)

    def save(self):
        """ commit all changes of current database 
        """
        sesh.commit(self)
    def delete(self, obj=None):
        """ delete from current database
        """
        obj.delete('fetch')
    def reload(self):
        """ create all tables and create current database
        """
        from Base import Base.metadata
        #Base.metadata.create_all(engine)
        sesh1 = sessionmaker(bind=eng, expire_on_commit=False)
        scped = scoped_session(sesh1) 
