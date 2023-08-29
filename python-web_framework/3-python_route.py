#!/usr/bin/python3
""" task on flask"""
from flask import Flask
app = Flask(__name__)


# this rout by default called when run it
@app.route("/", strict_slashes=False)
def display():
    # this is the method to dispaly message for user
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def show_message():
    # Dispaly HBNB message for user
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def show_C(text):
    # this is the method2 to dispaly message for user
    return("C {}".format(text.replace("_", " ")))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    # Display C with text for user
    return("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
