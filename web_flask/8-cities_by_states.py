#!/usr/bin/python3

if __name__ == "__main__":
    import os
    from models import storage
    from models.state import State
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.teardown_appcontext
    def close_app(i=None):
        storage.close()

    @app.route('/cities_by_states', strict_slashes=False)
    def city_state():
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            city = list(storage.all("State").values())
        else:
            city = State.city()
        return render_template('8-cities_by_states.html', city=city)

    app.run(host='0.0.0.0')
