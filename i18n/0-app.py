#!/usr/bin/env python3
'''Basic Flask App'''
from flask import flask, render_template



app = Flask()

@app.route("/")
def index():
    '''INDEX PAGE'''
    return(render_template('0-index.html'))
