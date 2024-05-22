#!/usr/bin/python3
""" Starts a web flask app """
from flask import Flask, render_template
from models import storage
from models.state import state
web_app = Flask(__name__)


@web_app.route('/states_list', strict_slashes=False)
def states_list():
    """ loads template states"""
    state_list =  storage.all("State")
    return render_template("7-states_list.html", state_list=state_list)


@web_app.teardown_appcontext
def teardown(arg=None):
    """ Close current session"""
    storage.close()


if __name__ == "__main__":
    web_app.run("0.0.0.0")
