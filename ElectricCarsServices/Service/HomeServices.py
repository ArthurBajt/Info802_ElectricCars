from flask import Blueprint, render_template


app: Blueprint = Blueprint('home', __name__, url_prefix='/')


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")
