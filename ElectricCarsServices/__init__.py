from flask import Flask

from .Service import services


app: Flask = Flask(__name__)

for bp in services:
    app.register_blueprint(bp)
