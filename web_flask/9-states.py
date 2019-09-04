#!/usr/bin/python3
from flask import Flask, render_template
import sys
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def return_states():
    states = storage.all("State").values()
    return render_template('9-states.html', states=states, selected="Only")


@app.route('/states/<id>', strict_slashes=False)
def return_cities(id):
    states = storage.all("State").values()
    for state in states:
        if str(state.id) == id:
            return render_template('9-states.html', states=state,
                                   selected="State")
    return render_template('9-states.html', states='None', selected="None")


@app.teardown_appcontext
def close_down(i=None):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
