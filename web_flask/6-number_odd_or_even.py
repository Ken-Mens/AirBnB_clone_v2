#!/usr/bin/python3
""" starts a flask web applicaton
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_is(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    if isinstance(n, int):
        if n & 1:
            m = 'odd'
        else:
            m = 'even'
    return render_template('6-number_odd_or_even.html', n=n, m=m)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
