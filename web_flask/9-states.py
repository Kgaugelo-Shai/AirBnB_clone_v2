#!/usr/bin/python3
"""Starts a Flask web app
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Gets an HTML page with a list of all States.
    """
    state_list = storage.all(State)
    return render_template("9-states.html", states=state_list)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """gets an HTML page with info about <id>, if it exists."""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """close current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
