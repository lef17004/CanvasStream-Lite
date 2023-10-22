from flask import Flask, render_template, url_for, request
from markupsafe import escape
from src.main import Main
from src.event import ClientToServer

applications = {}

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/setup/", methods=['POST'])
def setup():
    setup_info = request.get_json()
    main = Main()
    response = main.setup(setup_info)
    session_key = main.session_key
    applications[session_key] = main

    return response.instructions

@app.route("/event/<session_key>", methods=['POST'])
def event(session_key):
    print(session_key)
    message = ClientToServer(request.get_json())
    response = applications[str(session_key)].loop(message)
    return response.instructions

@app.route("/disconnect/<session_key>")
def disconnect(session_key):
    print('disconnect')
    return {}

@app.route("/image")
def image():
    return {
        "url" : url_for('static', filename='images/invader.png')
    }