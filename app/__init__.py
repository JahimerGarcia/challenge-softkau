from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
# toca importar los modelos despues porque me da error
# aun no encuentro como hacerlo optimo
from . import models


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    return app
