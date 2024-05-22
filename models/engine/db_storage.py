#!/usr/bin/python3
""" Storage engine for database """

from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class_list = { "Place": Place, "City": City,"Amenity": Amenity,
               "Review": Review, "User": User, "State": State}


class DBStorage:
    """ Storage engine for database, using mysql
    Attributes:
        __engine (sqlalchemy engine) : set to none
        __session (sqlalchemy session) : set to none
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Creates a new instance of DBStorage """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                       ), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session) all objects
            depending of the class name (argument cls)
        """
        dictionary = {}
        if cls is None:
            for cls in class_list.values():
                instances = self.__session.query(cls).all()
                for inst in instances:
                    key = inst.__class__.__name__ + '.' + inst.id
                    dictionary[key] = inst
        else:
            instances = self.__session.query(cls).all()
            for inst in instances:
                key = inst.__class__.__name__ + '.' + inst.id
                dictionary[key] = inst

        return dictionary

    def new(self, obj):
        """ Adds object in the current database session """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as error_thrown:
                self.__session.rollback()
                raise error_thrown

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current databse session the obj
            if it is not None
        """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session)()


    def close(self):
        """ calls remove() method on the priate session attribute
            (self.__session) or close() on the class Session
        """
        self.__session.close()
