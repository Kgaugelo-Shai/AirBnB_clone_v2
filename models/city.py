#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import hbnb_storage_type


class City(BaseModel):
    """ The city class, contains state ID and name """
    __table__ = 'cities'

    if hbnb_storage_type == 'db':
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
    else:
        name = ''
        state_id = ''
