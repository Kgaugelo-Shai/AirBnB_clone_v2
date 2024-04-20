#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import hbnb_stoarage_type


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    if hbnb_torage_type == 'db':
        name = Column(String(128),
                      nullable=False)
        cities = relationship('City',
                              backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        """returns the list of City instances with state_id equals the current
           State.id =>
           It will be a FileStorage relationship between State and City
        """
        cities_related = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                cities_related.append(city)
        return cities_related
