#!/usr/bin/python3
"""This is DB_Storage Engine"""
from os import getenv
from models.base_model import BaseModel, Base
#from models.amenity import Amenity
from models.city import City
#from models.place import Place
#from models.review import Review
from models.state import State
#from models.user import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import class_mapper
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
            Base.metadata.drop_all(bind=self.__engine)
    def all(self, cls=None):
        """ method that returns everyting based on class name
        """
        my_dict = {}
        self.__session = sessionmaker(bind=self.__engine)
        sesh = self.__session()
        if cls == None:
            for key, value in sesh.query(State, City).all():
                my_dict[cls.__name__] = value
        else:
            for key, value in sesh.query(cls.__name__):
                if key.startswith(cls.__name__):
                    my_dict[cls.__name__] = value
        return my_dict

    def new(self, obj):
        """ add object to current database
        """
        #for k, v in self.__object.items():
        self.__session = sessionmaker(bind=self.__engine)
        sesh = self.__session()
        sesh.add(obj)
    def save(self):
        """ commit all changes of current database 
        """
        sesh = self.__session()
        sesh.commit()
    def delete(self, obj=None):
        """ delete from current database
        """
        obj.delete('fetch')
    def reload(self):
        """ create all tables and create current database
        """
        #Session = sessionmaker(bind=self.__engine)
        eng = Base.metadata.create_all(self.__engine) 
        #Base.metadata.create_all(engine)
        sesh1 = sessionmaker(bind=eng, expire_on_commit=False)
        scped = scoped_session(sesh1) 
