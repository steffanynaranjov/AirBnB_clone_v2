#!/usr/bin/python3
"""Script that starts a Flask web application"""

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
def text(text):
    """C"""
    return "C {}".format(text).replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Python"""
    tex = text.replace('_', " ")
    return "Python {}". format(tex)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
