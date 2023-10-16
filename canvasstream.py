from flask import Flask, render_template, url_for, request
from markupsafe import escape
from src.main import CanvasStreamController

controllers = {}

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/connect")
def connect():
    global controllers
    new_controller = CanvasStreamController()
    session_key = new_controller.on_connect()
    controllers[session_key] = new_controller
    return {
        "sessionKey": session_key,
    }

@app.route("/setup/<session_key>", methods=['POST'])
def setup(session_key):
    # print(request.get_json())
    print(session_key)
    setup_info = controllers[session_key].on_setup(request.get_json())
    return setup_info

@app.route("/preloadAssets/<session_key>", methods=['POST'])
def preload_assets(session_key):
    return {}

@app.route("/canvas/<session_key>")
def canvas(session_key):
    return {}

@app.route("/event/<session_key>", methods=['POST'])
def event(session_key):
    print(request.get_json())
    return {}

@app.route("/disconnect/<session_key>")
def disconnect(session_key):
    return {}

@app.route("/image")
def image():
    return {
        "url" : url_for('static', filename='images/invader.png')
    }