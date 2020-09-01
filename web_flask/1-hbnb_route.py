#!/usr/bin/python3
"""task 0"""
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def home():
        """home function"""
        return "Hello HBNB!"

    @app.route("/hbnb", strict_slashes=False)
    def hbnb():
        """home function"""
        return "HBNB"
    app.run(host="0.0.0.0", port=5000)
