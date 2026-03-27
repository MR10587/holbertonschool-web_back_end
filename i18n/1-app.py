#!/usr/bin/env python3
'''Basic Flask App'''
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    app.config["BABEL_DEFAULT_LOCALE"] = "en"
    app.config["BABEL_DEFAULT_TIMEZONE"] = "UTC"


@app.route("/")
def index():
    '''INDEX PAGE'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
