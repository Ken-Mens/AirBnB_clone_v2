#!/usr/bin/python3
"""This is DB_Storage Engine"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models import State
from models.city import City
from sqlalchemy import create_engine
class DBStorage:
    """SQL STORAGE ENGINE
    """
    __engine = None
    __session = None

    def __init__(self):
        """ create the engine
        """
        user= getenv("HBNB_MYSQL_USER")
        password= getenv("HBNB_MYSQL_PWD")
        localhost= getenv("HBNB_MYSQL_HOST")
        database=  getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password,localhost, database, pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=engine)
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
        Session = sessionmaker(bind=self.__engine)
        sesh = Session()
        eng = Base.metadata.create_all(self.__engine) 
        #Base.metadata.create_all(engine)
        sesh1 = sessionmaker(bind=eng, expire_on_commit=False)
        scped = scoped_session(sesh1) 
