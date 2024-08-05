#!/usr/bin/python3
"""
Module defines Database engine `DBStorage`
"""
import os
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


# get the environ variabes
user = os.getenv('HBNB_MYSQL_USER')
passwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
hbnb_env = os.getenv('HBNB_ENV')


class DBStorage:
    """ Defines database engine """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize database instance """
        conn_string = "mysql+mysqldb://{}:{}@{}/{}".format(
                      user, passwd, host, db)
        self.__engine = create_engine(conn_string, pool_pre_ping=True)

        if hbnb_env == "test":
            # Drop all tables if test environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects if cls is None or objects of specified class
        """
        objs_dict = {}
        if cls:
            # Handle class
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs_dict[key] = obj
        else:
            # Handle all classes
            cls_list = [State, City, User, Review, Place, Amenity]
            for cls in cls_list:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """ Add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables and the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """ Removes the current session """
        self.__session.remove()

    def get(self, cls, id):
        """ Retrieve a specified object from storage """
        if cls is None or id is None:
            return None
        return self.__session.query(cls).get(id)

    def count(self, cls=None):
        """ Counts the all objects or class objects in storage """
        class_list = [State, City, Amenity, Place, User, Review]
        num_objs = 0
        if cls is None:
            for clss in class_list:
                num_objs += self.__session.query(clss).count()
        else:
            num_objs += self.__session.query(cls).count()

        return num_objs
