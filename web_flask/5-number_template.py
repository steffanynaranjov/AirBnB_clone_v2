#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
