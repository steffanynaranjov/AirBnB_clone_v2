#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import render_template
from models.state import State
from models import storage
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_hbnb():
    """HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def var(text):
    """C"""
    tex = text.replace('_', ' ')
    return "C {}".format(tex)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Python"""
    tex = text.replace('_', " ")
    return "Python {}". format(tex)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Number template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """Number odd/even template"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display States"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
