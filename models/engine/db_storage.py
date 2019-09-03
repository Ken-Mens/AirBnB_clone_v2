#!/usr/bin/python3
"""This is DB_Storage Engine"""
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
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
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        localhost = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, localhost,
                                             database, pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ method that returns everyting based on class name
        """
        my_dict = {}
        sesh = self.__session()
        if cls is None:
            tables = [Amenity, City, Place, State, Review, User]
            for table in tables:
                my_query = sesh.query(table).all()
                for res in my_query:
                    my_dict[(str(res.__class__.__name__) + "." +
                             str(res.id))] = res
        else:
            my_query = sesh.query(eval(cls)).all()
            for res in my_query:
                my_dict[str(res.__class__.__name__) + "." + str(res.id)] = res
        return my_dict

    def new(self, obj):
        """ add object to current database
        """
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
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables and create current database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """ closes out private session attribute
        """
        self.__session.close()
