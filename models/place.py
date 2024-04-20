#!/usr/bin/python3
""" Place Module """

from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from os import getenv
import models


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ Defines a Place class """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60),
                         ForeignKey('cities.id'),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
        name = Column(String(128),
                      nullable=False)
        description = Column(String(1024),
                             nullable=True)
        number_rooms = Column(Integer,
                              nullable=False,
                              default=0)
        number_bathrooms = Column(Integer,
                                  nullable=False,
                                  default=0)
        max_guest = Column(Integer,
                           nullable=False,
                           default=0)
        price_by_night = Column(Integer,
                                nullable=False,
                                default=0)
        latitude = Column(Float,
                          nullable=True)
        longitude = Column(Float,
                           nullable=True)
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ gives a list of review instances
            """
            all_rv = storage.all(Review)
            rv_list = []
            for rv in all_rv.values():
                if rv.place_id == self.id:
                    rv_lst.append(rv)
            return rv_lst

        @property
        def amenities(self):
            """ gives list of Amenity instances
            """
            am_list = []
            all_amenities = storage.all(Amenity)
            for a in all_amenities.values():
                if a.id in self.amenity_ids:
                    am_list.append(a)
            return am_list

        @amenities.setter
        def amenities(self, obj):
            ''' adds amenity_id
            '''
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
