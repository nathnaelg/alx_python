#!/usr/bin/python3
""" First task on flask"""

from flask import Flask

app = Flask(__name__)


# this rout by default called when run it
@app.route("/", strict_slashes=False)
def display():
    # this is the method to dispaly message for user
    return("Hello HBNB!")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
