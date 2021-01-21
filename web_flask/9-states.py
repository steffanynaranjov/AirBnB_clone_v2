#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ clse the session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_all():
    """Display States"""
    states = storage.all(State)
    return render_template('9-states.html', state=states, mode="none")


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """Display States"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode="id")
    else:
        return render_template('9-states.html', states=state, mode="not")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
