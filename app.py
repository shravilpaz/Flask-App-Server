from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'
