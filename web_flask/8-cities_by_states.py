#!/usr/bin/python3
"""task 8"""
from flask import Flask, render_template
import models


if __name__ == "__main__":
    app = Flask(__name__)

    @app.teardown_appcontext
    def teardo_db(session):
        """close session"""
        models.storage.close()

    @app.route("/cities_by_states", strict_slashes=False)
    def stateslist():
        """cities_by_states displaying"""
        l = models.storage.all(models.state.State).values()
        return render_template("8-cities_by_states.html", states=l)

    app.run(host="0.0.0.0", port=5000)
