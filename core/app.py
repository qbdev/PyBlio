"""Base module for the Flask app"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Route for the index: /
    Missing at the time being"""
    return "Hello World!"
