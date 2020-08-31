#!/usr/bin/python3
"""task 3"""
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def home():
        """the home directory displaying"""
        return "Hello HBNB!"

    @app.route("/hbnb", strict_slashes=False)
    def hbnb():
        """the hbnb directory displaying"""
        return "HBNB!"

    @app.route("/c/<string:f>", strict_slashes=False)
    def cisfun(f):
        """
        the c directory displaying
        replacing "_" by " "
        """
        return "C " + f.replace("_", " ")

    @app.route("/python", strict_slashes=False)
    @app.route("/python/<string:f>", strict_slashes=False)
    def pythondisplay(f=None):
        """
        the python directory displaying
        replacing "_" by " "
        """
        if f is None:
            return "Python is cool"
        else:
            return "Python " + f.replace("_", " ")

    app.run(host="0.0.0.0", port=5000)
