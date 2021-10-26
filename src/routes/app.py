import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    call_me()  # Maybe

    return "Hello World!"


@app.route('/error')
def error():
    raise ValueError("1 != 0")


@app.route('/external')
def external_call():    
    req = requests.get('http://localhost:8000/external/source')
    req.raise_for_status()

    return " ".join(("External:", req.text))


@app.route('/external/source')
def external_source():
    return "Hello, fellow humans!\n"


@app.route('/external/error')
def external_error():
    req = requests.get('http://localhost:8000/error')
    req.raise_for_status()

    return req.text


def call_me(i=3):
    if i <= 0:
        return other_function()
    return call_me(i-1)


def other_function():
    print("Hello")
    return 3
