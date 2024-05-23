#!/usr/bin/python3
""" starts a web app in flask using two routes
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
web_app = Flask(__name__)


@web_app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns template with states"""
    state_list = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=state_list, amenities=amenities)


@web_app.teardown_appcontext
def teardown(arg=None):
    """ closes currenyt session"""
    storage.close()


if __name__ == '__main__':
    web_app.run(host='0.0.0.0')
