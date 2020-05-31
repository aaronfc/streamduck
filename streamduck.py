from subprocess import Popen, PIPE
from time import sleep
from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def shortcut(shortcut):
    Popen("xdotool keydown " + shortcut, stdout=PIPE, shell=True).stdout.read()
    sleep(0.15)
    Popen("xdotool keyup " + shortcut, stdout=PIPE, shell=True).stdout.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/goto/<place>', methods=['POST'])
def goto(place):
    mapping = {
        "intro": "ctrl+alt+0",
        "brb": "ctrl+alt+8",
        "coding": "ctrl+alt+1",
        "talking": "ctrl+alt+2",
    }
    shortcut(mapping[place])
    shortcut('ctrl+alt+KP_Insert')
    return "{success: true}"

@app.route('/action/mute', methods=['POST'])
def action_mute():
    shortcut('ctrl+alt+3')
    return "{success: true}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
