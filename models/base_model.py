#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
import models
from os import getenv


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    Attributes:
        id (String sqlalmemy): The BaseModel unique id
        created_at (DateTime sqlalchemy) : The datetime obj at creation
        updated_at (DateTime sqlalchemy) : The datetime obj on the last update
    """

    id = Column(String(60),
                nullable=False,
                primary_key=True,
                unique=True)
    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instantiates a new Base model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                elif key == 'created_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                attr_ls = {
                    'id' : str(uuid.uuid4()),
                    'created_at' : datetime.now(),
                    'updated_at' : datetime.now()
                    }
                for k,v in attr_ls.items():
                    if not hasattr(kwargs, k):
                        setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__

        # Iterate over dictionary items
        for k, v in dictionary.items():
            # Convert datetime objects to string format
            if isinstance(v, datetime):
                dictionary[k] = v.isoformat()

        # Remove '_sa_instance_state' key if present
        if '_sa_instance_state' in dictionary:
                del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """ Deletes the current instance from the storage (model.storage)
        """
        storage.delete(self)
