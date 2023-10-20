from flask import Flask, render_template, url_for, request
from markupsafe import escape
from src.main import Main

applications = {}

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/setup/", methods=['POST'])
def setup():
    # print(request.get_json())
    setup_info = request.get_json()
    main = Main()
    response = main.setup(setup_info)
    session_key = str(response['sessionkey'])
    applications[session_key] = main
    print(session_key)
    return response

@app.route("/event/<session_key>", methods=['POST'])
def event(session_key):
    
    response = applications[str(session_key)].loop(request.get_json())
    return response

@app.route("/disconnect/<session_key>")
def disconnect(session_key):
    return {}

@app.route("/image")
def image():
    return {
        "url" : url_for('static', filename='images/invader.png')
    }