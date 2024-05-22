#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def flask_greeting():
    """ Display greeting """
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def flask_greeting2():
    """ Display greeting"""
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ formated text returned as a string"""
    return 'C ' + text.replace('_', ' ')


if __name__ == "__main__":
    web_app.run('0.0.0.0')
