#!/usr/bin/python
""" Starts a Flask web application
    Listens on 0.0.0.0, port 5000
"""
from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def app_respone():
    """ Displays greeting 'Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    web_app.run(host="0.0.0.0")
