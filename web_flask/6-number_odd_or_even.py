#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
from flask import render_template
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


@web_app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """ returns an html page if n is an integer """
    return render_template("5-number.html", n=n)


@web_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ Displays an html page if n is integer, also displays if even or odd """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    web_app.run('0.0.0.0')
