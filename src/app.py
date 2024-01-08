import os
from flask import Flask, jsonify

# App Initialization
app = Flask(__name__)

# Hello World!
@app.route('/')
def hello():
    return "Hello World!"

from . import url

if __name__ == "__main__":
    app.run()