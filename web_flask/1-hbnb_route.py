#!/usr/bin/python3
""" starts a flask web applicaton
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run()
