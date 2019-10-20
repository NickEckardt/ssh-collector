#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#@app.route('/servers')
#def hello_world():
#    return 'No servers online, nerd'
