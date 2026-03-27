#!/usr/bin/env python3
from flask import flask, render_template


app = Flask()

@app.route("/")
def index():
    return render_template("0-index.html")
