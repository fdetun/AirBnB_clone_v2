#!/usr/bin/python3
"""task 4"""
from flask import Flask, render_template


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

    @app.route("/number/<int:f>", strict_slashes=False)
    def numberdisplay(f):
        """
        the c directory displaying
        replacing "_" by " "
        """
        return "{:d} is a number".format(f)

    @app.route("/number_template/<int:f>", strict_slashes=False)
    def templdisplay(f):
        """
        the c directory displaying
        replacing "_" by " "
        """
        return render_template("5-number.html", n=n)

    app.run(host="0.0.0.0", port=5000)
