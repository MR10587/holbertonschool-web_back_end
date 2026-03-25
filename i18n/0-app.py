from flask import flask, render_template


app = Flask()

@app.route("/")
def index():
    return render_template("index.html")
