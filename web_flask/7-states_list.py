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

    @app.route("/states_list", strict_slashes=False)
    def stateslist():
        """states_list displaying"""
        states = models.storage.all(models.state.State).values()
        return render_template("7-states_list.html", states=states)

    app.run(host="0.0.0.0", port=5000)
