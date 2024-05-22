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


@web_app.route("/python/", strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def py_greeting(text="is cool"):
    """ Displays python followed by value of text """
    return "Python " + text.replace("_", " ")


@web_app.route("/number/<int:n>", strict_slashes=False)
def num_display(n):
    """ returns 'n is a number' is n is integer """
    return "{} is a number".format(n)


if __name__ == "__main__":
    web_app.run('0.0.0.0')
