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
#SHA256:WwtMaSoOwksjPNypH9lwxkc23chdmkwFo2TfTtfUWhU luisgranton04@gmail.com
